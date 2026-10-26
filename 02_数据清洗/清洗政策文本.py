# -*- coding: utf-8 -*-
import pandas as pd

# 处理
def deal(i):
    # 1 切片
    l_idx = 0
    r_idx = len(i) + 1
    x0 = '扫一扫在手机打开当前页'
    x1 = '订阅 订阅更多'
    x2, x21 = '号\n', '宁科通'
    x3, x4 = '阅读原文 ', '阅读量'
    x5, x6, x7, x8 = '>>>企业信息一键对比，点击一下，快速了解企业差异<<<', '>>>如需查询更多的通过名单，请点击阅读原文<<<', '科技政策推送查讯', '科技政策推送查询'

    # 1.1 确定切片左idx
    if x1 in i:
        l_idx = i.index(x1) + len(x1)
    elif x21 in i and x2 in i:
        l_idx = i.index(x2) + len(x2)

    if i[0] == '【':
        i = i.replace(x5, '')
        i = i.replace(x6, '')
        if x7 in i:
            l_idx = i.index(x7) + len(x7)
        if x8 in i:
            l_idx = i.index(x8) + len(x8)
    # 1.2 确定切片右idx
    if x0 in i:
        r_idx = i.index(x0)
    elif x3 in i and x4 in i:
        r_idx = i.index(x3)
    elif x4 in i:
        r_idx = i.index(x4)
    y = i[l_idx:r_idx]

    # 2 分行处理
    y1 = y.splitlines()
    y2 = []
    for i in y1:
        if i != '' and i != '\xa0':
            if i != '\t':
                y2.append(i)
    y3 = '\n'.join(y2)
    # 3 针对展示政策2.csv文件格式增加处理
    # rl1 = '　　'
    # rl2 = '  '
    # if rl1 in y3:
    #     y3 = y3.replace(rl1, '\n')
    # if rl2 in y3:
    #     y3 = y3.replace(rl2, '\n')
    return y3

if __name__ == '__main__':
    # 1 读取
    path = '/Users/zhangduola/Desktop/展示政策1.csv'
    cnt = pd.read_csv(path)
    pid, txt = list(cnt['序号']), list(cnt['文本'])
    # 2 处理
    pid_n = []
    txt_n = []
    for p, t in zip(pid, txt):
        pid_n.append(p)
        txt_n.append(deal(t))
        print(f'第{p+1}条数据清洗完毕！')
    # 3 写入
    df = pd.DataFrame(data={'序号': pid_n, '文本': txt_n})
    df.to_csv('清洗文本1.csv', index=False)




