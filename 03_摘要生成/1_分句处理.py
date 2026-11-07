# -*- coding: utf-8 -*-

import pandas as pd

# 将清洗后的政策正文转换为逐行排列的句子，供后续摘要处理使用。
def trans(txt):
    st = []

    # 1 以。分割，并去除''和''\xa0'形式的元素
    for i in txt.splitlines():
        i = i.split('。')
        remo = ['', '\xa0']
        for z in remo:
            if z in i:
                while 1:
                    i.remove(z)
                    if z not in i:
                        break
        st.extend(i)

    # 统一句末标点，避免下游处理时混用冒号、分号与句号。
    # 2 去除句子两旁空格 并 保证句末为句号
    for i in range(len(st)):
        st[i] = st[i].strip()
        if st[i]:
            flag = 0
            rem = ['：', '；', '。']
            for j in rem:
                if st[i][-1] == j:
                    st[i] = st[i].replace(j, '。')
                    flag = 1
            if not flag:
                st[i] += '。'

    # 3 strip()后会含有''，去除
    while '' in st:
        st.remove('')

    # 4 用\n将句子连接
    st = '\n'.join(st)
    return st

if __name__ == '__main__':
    # 1 读取
    cnt = pd.read_csv('清洗数据/清洗文本.csv')
    pid, txt = list(cnt['序号']), list(cnt['文本'])
    # 按政策序号单独输出文本文件，便于后续逐文档处理。
    # 2 处理并写入
    for x, y in zip(pid, txt):
        with open('res/' + str(x) + '.txt', 'x') as f:
            f.write(trans(y))
        print('第' + str(x) + '条数据写入完毕!')
