# -*- coding: utf-8 -*-

import os

def read_dir(path):
    fileArray = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray

def delete_numlabel(i, j):
	f = open(i, 'r+', encoding="utf8", errors='ignore')
	strContents = ''
	while True:
		l = f.readline()
		if l == '\n':
			continue
		if len(l) == 0:
			break
		flag = 0
		for z in ['。', '.', '）', '、', '．']:
			dotIndex = l.find(z)
			if dotIndex != -1 and dotIndex < 4:
				flag += 1
				l = l[dotIndex + 1:]
				l = l.lstrip(' ')
				if l == '\n':
					continue
				strContents += l

		if not flag:
			strContents += l
	f.close()

	strContents.expandtabs(4)
	f2 = open(j, 'x')
	f2.write(strContents)
	f2.close()

if __name__ == '__main__':
	file = read_dir('/Users/zhangduola/Desktop/tes/res')
	for i in file:
		j = i.replace('res', 'res2')
		delete_numlabel(i, j)



