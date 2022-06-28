# -*- coding = utf-8 -*-
# @Time :2022/6/28 17:29
# @Author:HANG
# @File : list_zy.py
# @Software: PyCharm

# 作业：
# 现有商品列表如下：
# 1. products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],
# ["Nike",699]]，需打印出以下格式：

# ------ 商品列表 ------
# 0 iphone 6888
# 1 MacPro 14800
# 2 小米6 2499
# 3 Coffee 31
# 4 Book 60
# 5 Nike 699
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

for product in products :
    #print(products.index(product))
    #for pro in product:
        print(products.index(product),product[0],product[1])



# 2. 根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应
# 的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。

buy = [];

useinput = input("请输入您想购买的序号：")

selProduct = products[int(useinput)]

#print(buy.append(selProduct))
print("您已经选购的商品如下：")
print(selProduct)

# gproduce=[]    #购买的商品列表
# while True:
#     num=input("请输入你想购买的商品号：")
#     if num=="q":
#         break
#         #当输入商品号不正确的提示
#     if int(num)!=0 and int(num)!=1 and int(num)!=2 and int(num)!=3 and int(num)!=4 and int(num)!=5:
#         print("你选的商品号没有，请输入正确的商品号：")
#         continue
#     gproduce.append(int(num))
# print("您已经选购的商品如下：")
# print("商品编号","商品名","商品价格")
# for g in gproduce:
#     print(g,end="    ")
#     for x in products[g]:
#         print(x,end="    ")
#     print()
