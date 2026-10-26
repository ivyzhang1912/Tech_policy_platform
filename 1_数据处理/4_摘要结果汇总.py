# -*- coding: utf-8 -*-

import pandas as pd
import os

# 获取path文件夹内的所有文件地址，返回列表
def read_dir(path):
    fileArray = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray

if __name__ == '__main__':
    file = read_dir('/Users/zhangduola/Desktop/data_progress/2添加摘要/输出')
    abstract = [''] * 3029
    pid = []
    for i in file:
        if '.DS_Store' in i:
            continue
        l_idx = i.find('输出/') + 3
        r_idx = i.find('.txt')
        idx = int(i[l_idx:r_idx])
        abst = open(i).read()
        abstract[idx - 1] = abst
    pid = []
    abstract_ = []
    for x, y in enumerate(abstract):
        pid.append(x+1)
        abstract_.append(y)

    df = pd.DataFrame(data = {'序号': pid, '摘要': abstract})
    df.to_csv('/Users/zhangduola/Desktop/data_progress/2添加摘要/摘要.csv', index=False)

