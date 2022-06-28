# -*- coding = utf-8 -*-
# @Time :2022/6/28 16:29
# @Author:HANG
# @File : list.py
# @Software: PyCharm

# namesList = ['xiaoWang','xiaoZhang','xiaoHua']
#
#
# print(namesList[0:3])
#
# for name in namesList:
#     print(name)
#
#     print(namesList.index(name))

# 列表的嵌套

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

# 定义一个列表保存三个办公室
import random

import random
# 定义一个列表用来保存3个办公室
offices = [[],[],[]]
# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']
i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)