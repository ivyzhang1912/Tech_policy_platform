import os
from flask import Flask
import requests
import json
import pymysql
from flask_cors import CORS
from time import *
from decimal import Decimal
from datetime import datetime, date

app = Flask(__name__)

# 连接数据库
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": os.getenv("DB_PASSWORD", ""),
    "database": "tech_policy"
}
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
print('ok')

# 登陆并将用户数据存入user表中
@app.route('/login/<code>')
def login(code):
    # 1 传入code，获得用户唯一openid
    # print(code)
    data = {
        'appid': 'wxf48284e0d29d9b68',
        'secret': os.getenv("WX_APPSECRET", ""),
        'js_code': code
    }
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    r = requests.post(url, data=data)
    print(r.text)
    openid = eval(r.text)['openid']
    # 2 先查询是否user表中已存在该用户
    sql = "select uid from user where openid = %s"
    cursor.execute(sql, openid)
    data = cursor.fetchone()
    # 3 若不存在该用户，则插入该用户
    if (not data):
        sql = 'INSERT INTO user(openid) VALUES(%s)'
        cursor.execute(sql, openid)
        db.commit()
    # cursor.close()
    # db.close()
    return r.text

# 读取热门政策
@app.route('/gethotpolicy')
def gethotpolicy():
    cursor.execute("select pid, title, department, datetime from policy limit 20")
    data = cursor.fetchall()
    print(1111)
    return json.dumps(data)

# 设置content页（1 获取内容 2 查看star情况 3 添加进该用户的浏览记录）
@app.route('/getcontent/<openid>/<int:pid>')
def getcontent(openid, pid):
    # 1 获取内容
    sql = 'select * from policy where pid = %s'
    cursor.execute(sql, pid)
    cnt = cursor.fetchall()
    cnt = cnt[0]
    print('——————————————————已经获取内容——————————————————')
    # 2 查看star情况
    # 2.1 获取该用户uid
    sql = "select uid from user where openid = %s"
    cursor.execute(sql, openid)
    data = cursor.fetchone()
    uid = data['uid']
    # 2 返回是否star
    sql = "select uid from star where uid = %s and pid = %s"
    cursor.execute(sql, (uid, pid))
    data = cursor.fetchall()
    if not data:
        cnt['flag'] = 'false'
    else:
        cnt['flag'] = 'true'
    print('——————————————————已经获取star——————————————————')

    # 3 添加进该用户的浏览记录
    # 3.1 查询该用户是否已经拥有该浏览记录
    sql = "select uid from record where uid = %s and pid = %s"
    cursor.execute(sql, (uid, pid))
    data = cursor.fetchall()
    # 3.2 若不存在该记录则插入记录(uid pid time)
    if (not data):
        sql = "insert into record values(%s, %s, CURRENT_TIMESTAMP, %s)"
        cursor.execute(sql, (uid, pid, 1))
        db.commit()
    # 3.3 否则更新浏览记录时间
    else:
        sql = "update record set time = CURRENT_TIMESTAMP where uid = %s and pid = %s"
        cursor.execute(sql, (uid, pid))
        db.commit()
        sql = "update record set count = count + 1 where uid = %s and pid = %s"
        cursor.execute(sql, (uid, pid))
        db.commit()
    print('——————————————————已经添加浏览记录——————————————————')

    def update(pk, pw, k, w, uid):
        sql = 'update user set prefer=%s where uid=%s'
        for i in range(len(pk)):
            for j in range(len(pk[i])):
                try:
                    a = k.index(pk[i][j])
                    w[a] += pw[i][j]
                except:
                    k.append(pk[i][j])
                    w.append(pw[i][j])
        dic = dict(zip(k, w))
        mid = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        midk = []
        midw = []
        for i in mid[:10]:  # 保留十个关键词
            midk.append(i[0])
            midw.append(i[1])
        result = dict(zip(midk, midw))
        print('更新该用户prefer为', result)
        cursor.execute(sql, (str(result), uid))
        db.commit()

    def weightc(pid, pk, pw, k, w):
        score = []
        result = []
        for i in range(len(pk)):
            w1 = 0
            for j in range(len(pk[i])):
                try:
                    a = k.index(pk[i][j])
                    w1 += w[a] * pw[i][j]
                except:
                    w1 += 0
            score.append(w1)
        # print(score)
        dic = dict(zip(pid, score))
        # print(dic)
        mid = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for m in mid:
            result.append(m[0])
        return result

    def insert_result(uid, result):
        sql0 = 'delete from push where uid = %s'
        sql = 'insert into push(uid,pid) values(%s,%s)'
        cursor.execute(sql0, uid)
        for i in range(20):  # 推送前二十条
            e = (uid, result[i])
            # print(e)
            cursor.execute(sql, e)
            db.commit()

    # 4 更新用户prefer
    sql = 'SELECT * FROM user where uid=%s'
    # SELECT * FROM user where uid=%s
    sql1 = 'select * from policy where pid in (select pid from record where uid=%s)'
    # select * from policy where pid in (select pid from record where uid=%s)
    cursor.execute(sql, uid)
    res = cursor.fetchone()
    cursor.execute(sql1, uid)
    res1 = cursor.fetchall()
    pk = []
    pw = []
    for i in res1:
        pkeywords = []
        pweight = []
        if i['tfidf'] == None:  # 部分政策tfidf为空，遇到该部分类型政策跳过
            continue
        k = list(eval(i['tfidf']).items())
        for j in k:
            pkeywords.append(j[0])  # 关键词
            pweight.append(j[1])  # 权重
        pk.append(pkeywords)
        pw.append(pweight)

    keywords = []
    weight = []
    try:
        k = list(eval(res['prefer']).items())
        for j in k:
            keywords.append(j[0])  # 关键词
            weight.append(j[1])  # 权重
    except:
        pass
    update(pk, pw, keywords, weight, res['uid'])
    print('——————————————————已经更新用户prefer——————————————————')

    # 5 更新push表
    cursor.execute('SELECT * FROM user where uid=%s', uid)
    res = cursor.fetchone()
    cursor.execute('select pid, tfidf from policy')
    res_p = cursor.fetchall()
    # print(res)
    # print(res_p)
    pk = []
    pw = []
    pid = []
    # 获取policy信息
    for i in res_p:
        pkeywords = []
        pweight = []
        pid.append(i['pid'])
        if i['tfidf'] == None:
            continue
        k = list(eval(i['tfidf']).items())
        for j in k:
            pkeywords.append(j[0])  # 关键词
            pweight.append(j[1])  # 权重
        pk.append(pkeywords)
        pw.append(pweight)

    # 6 结合用户prefer及文章tfidf推荐
    keywords = []
    weight = []
    if res['p'] == None:
        result = []
        res2 = cursor.execute('select * from policy limit 11, 20')
        for x in res2:
            result.append(x['pid'])
            insert_result(res['uid'], result)
    else:
        k = list(eval(res['prefer']).items())
        for j in k:
            keywords.append(j[0])  # 关键词
            weight.append(j[1])  # 权重
        # print(keywords)
        result = weightc(pid, pk, pw, keywords, weight)
        insert_result(res['uid'], result)
    print('——————————————————已经更新push表——————————————————')
    return json.dumps(cnt)

# add/delete star情况
@app.route('/adddeletestar/<openid>/<int:pid>/<flag>')
def adddeletestar(openid, pid, flag):
    print(flag)
    # 1 获取该用户uid
    sql = "select uid from user where openid = %s"
    cursor.execute(sql, openid)
    data = cursor.fetchone()
    uid = data['uid']
    # 2 判断flag
    if (flag == 'true'):
        sql = "insert into star values(%s, %s, CURRENT_TIMESTAMP)"
        cursor.execute(sql, (uid, pid))
        db.commit()
    else:
        sql = "delete from star where uid = %s and pid = %s"
        cursor.execute(sql, (uid, pid))
        db.commit()
    # cursor.close()
    return 'add/delete star ok'

@app.route('/getmine/<openid>/<mytype>')
def getmine(openid, mytype):
    # 1 获取该用户uid
    sql = "select uid from user where openid = %s"
    cursor.execute(sql, openid)
    data = cursor.fetchone()
    uid = data['uid']
    # 2 查询
    mytype = 'record' if mytype == '浏览记录' else 'star'
    sql = 'select pid, title, department, datetime from policy where pid in (select pid from %s where uid = %s);' % (
    mytype, uid)
    cursor.execute(sql)
    res = cursor.fetchall()
    # print(res)
    return json.dumps(res)

@app.route('/gettype/<cnt_type>/<type>/<t>/<area>')
def gettype(cnt_type, type, t, area):
    if area == '全部地区':
        if t == '全部时间':
            sql = "select pid, title, department, datetime from policy where cnt_type = %s and type = %s"
            cursor.execute(sql, (cnt_type, type))
        else:
            t = t[:-1]
            sql = 'select pid, title, department, datetime from policy where cnt_type = %s and type = %s and %s = left(datetime, 4)'
            cursor.execute(sql, (cnt_type, type, t))
        data = cursor.fetchall()
    else:
        area_l = area.split(',')
        if area_l[0] == '国家级':
            f = '全国'
        elif area_l[0] == '省市':
            if area_l[2]:
                f = f'{area_l[1]}省{area_l[2]}市'
            else:
                f = f'{area_l[1]}省'
        if t == '全部时间':
            sql = "select pid, title, department, datetime from policy where cnt_type = %s and type = %s and area = %s"
            cursor.execute(sql, (cnt_type, type, f))
        else:
            t = t[:-1]
            sql = 'select pid, title, department, datetime from policy where cnt_type = %s and type = %s and %s = left(datetime, 4) and area = %s'
            cursor.execute(sql, (cnt_type, type, t, f))
        data = cursor.fetchall()

    return json.dumps(data)

@app.route('/search/<ipt>/<area>')
def search(area, ipt):
    if area == '全部地区':
        sql = 'select pid, title, department, datetime from policy where title like "%' + ipt + '%"'
        cursor.execute(sql)
    else:
        area_l = area.split(',')
        if area_l[0] == '国家级':
            f = '全国'
        elif area_l[0] == '省市':
            if area_l[2]:
                f = f'{area_l[1]}省{area_l[2]}市'
            else:
                f = f'{area_l[1]}省'
        sql = 'select pid, title, department, datetime from policy where title like "%' + ipt + '%" and area ="' + f + '"'
        cursor.execute(sql)
    data = cursor.fetchall()
    return json.dumps(data)

@app.route('/push/<openid>/<int:value>')
def push(openid, value):
    # 1 获取该用户uid
    sql = "select uid from user where openid = %s"
    cursor.execute(sql, openid)
    data = cursor.fetchone()
    uid = data['uid']
    # 2 通过uid，获取push表pid列表
    sql = "select pid from push where uid = %s"
    cursor.execute(sql,uid)
    pid_l = cursor.fetchall()
    # 获取pid详细信息
    res = []
    for i in pid_l:
        sql = 'select pid, title, department, datetime, type from policy where pid = %s'
        cursor.execute(sql, i['pid'])
        d = cursor.fetchone()
        res.append(d)
    # 筛选相应type类型的信息
    if value == 0:
        ty = '政策通知'
    elif value == 1:
        ty = '政策解读'
    else:
        ty = '最新资讯'
    res_ty = []
    for j in res:
        if j['type'] == ty:
            res_ty.append(j)
    return json.dumps(res_ty)


if __name__ == '__main__':
    app.run()

