#!/usr/bin/env python
# coding: utf-8

# In[90]:


import os 
import xlrd
import jieba

def readdict(path):
    book = xlrd.open_workbook(path)
    sheet_names= book.sheet_names()
    for sheet_name in sheet_names:
        sheet = book.sheet_by_name(sheet_name)
        cols = sheet.col_values(1) 
    dic1=dict()
    n=0
    
    return cols


book=xlrd.open_workbook("清洗政策.xlsx")
s1=book.sheet_by_name("清洗政策")
cols=s1.col_values(6)

    
    
    
    
    
    
def fun(path):
    fileArray = []    
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray 

def BMM(worddict1,worddict2, maxWordLength, sentence):  #最大逆向匹配函数
    result = []
    while len(sentence) != 0:
        segWord = sentence[len(sentence)-maxWordLength:len(sentence)]
        while not(segWord in worddict1):   #在词表里面找词匹配形成分词
            if len(segWord) > 1:
                segWord = segWord[1:] 
            else:
                sentence = sentence[:len(sentence)-1]
                break
        if not (segWord in worddict2):#判断该分词是否属于停用词表里的词，不是的话计入结果（result）
            result.append(segWord)
        sentence = sentence[:len(sentence)-len(segWord)]
    return result

num=-1

for p in cols:  #分词阶段，对文件夹里的所有文本进行分词保存
    num+=1
    dict1=readdict("词表/words.xlsx")
    dict2=readdict("词表/stopwords.xlsx")
    result1=BMM(dict1,dict2,9,p)
    with open("结果2/txt"+str(num)+".txt",'w',encoding = 'utf-8') as fw:
        for r in result1:
            fw.write(r+"\n")
        fw.close()
    



# In[114]:


#弄成一堆txt
import os
import math
import operator
import openpyxl
wb = openpyxl.load_workbook("清洗政策.xlsx")
s=wb['清洗政策']
def fun(path):#遍历文件夹函数
    fileArray = []    
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray 
num=0
dic=dict()  #文档中的词频
tfidf=dict()
idf=dict()#有该词语的文档数
idfr=dict()#log(3030/有该词语的文档数)
tf=dict()#计算tf=文档内词频/文档内词语总数
l=dict()
dic2=dict()#总的词频
count=1
while count<=3029:#此处的结果指的是之前为每个文本分词得到的结果
    text="" 
    with open ('结果2/txt'+str(count)+".txt",'r',encoding='utf-8')as f:
        txt=f.readlines()
        
#             if i in dic2 :
#                 dic2[i]=dic2[i]+1
#             else:
#                 dic2[i]=1
#         with open ("词频/cp"+str(count)+".txt",'w',encoding='utf-8')as fw:
#             result1=sorted(dic.items(),key=lambda x:x[1],reverse=True) 
#             for j in result1:
#                 fw.write(str(j)+"\n")
#         fw.close()
        
      
            
            
        for i in txt:     
            if i in idf and  i not in l and i!="\n"and i!="	":
                idf[i]=idf[i]+1
                l[i]=1
            elif i not in l and i!="\n" and i!="	":
                idf[i]=1
                l[i]=1
        l.clear()
#         result2=sorted(idf.items(),key=lambda x:x[1],reverse=True)
#         with open ("idf/IDF"+str(count)+'.txt','w',encoding='utf-8')as fw2:    
#              for j in result2:
#                 fw2.write(str(j)+"\n")
#         fw2.close()
#         for i in dic:
#             for j in idf:
#                 if i==j:
#                     tfidf[i]=dic[i]/idf[i]
#         result3=sorted(tfidf.items(),key=lambda x:x[1],reverse=True)
#         with open ("tfidf/TF-IDF"+str(count)+'.txt','w',encoding='utf-8')as fw3:
#             for j in result3:
#                 fw3.write(str(j)+"\n")
#         fw3.close()       
    f.close()
    dic.clear()
    count+=1
count=1
while count<=3029:
    with open ('结果2/txt'+str(count)+".txt",'r',encoding='utf-8')as f:
            txt=f.readlines()
            for i in txt:
                if i in dic :
                    dic[i]=dic[i]+1
                else:
                    dic[i]=1
            for i in dic :
                if i!="\n"and len(txt)!=0:
                    tf[i]=dic[i]/len(txt)
            for i in txt :
                if  i != '\n':
                    tfidf[i]=tf[i]*math.log(3029/idf[i])
            result1=dict(sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True))  
            with open ("tfidf/TF-IDF"+str(count)+'.txt','w',encoding='utf-8')as fw3:
                k=0
                fw3.write("{")
                #s.cell(row=count,column=10).value=result1.items()[0:10]
                for j in result1.items():
                    if len(j[0])>2 and j[0]!="	\n" and j[0]!=" \n"and k < 9:
                        fw3.write("'"+str(j[0])[0:len(j[0])-1]+"':"+str(j[1])+",")
                        k+=1
                    elif len(j[0])>2 and k == 9 and j[0]!="	\n" and j[0]!=" \n":
                        fw3.write("'"+str(j[0])[0:len(j[0])-1]+"':"+str(j[1]))
                        k+=1
                    if k==10:                        
                        break
                fw3.write("}")
            fw3.close()
            tfidf.clear()
            tf.clear()
            count+=1
wb.save("清洗政策.xlsx")        


# In[115]:


import openpyxl
wb = openpyxl.load_workbook("清洗政策.xlsx")
s=wb['清洗政策']
def fun(path):#遍历文件夹函数
    fileArray = []    
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray 
count=2

for i in range(1,3030):
    with open ("tfidf/TF-IDF"+str(i)+".txt",'r',encoding='utf-8')as f:
        s.cell(row=count,column=12).value=f.read()
        count+=1
    f.close()
wb.save("清洗政策.xlsx")  


# In[ ]:




