# -*- coding = utf-8 -*-
# @Time :2022/6/28 10:46
# @Author:Hang
# @File : inputTest.py
# @Software: PyCharm

import keyword

import random

# print("hello world")
#
# print("你好，python")


# password = input("请输入密码：")
#
# print("您刚刚输入的密码是：%s"%(password))


# a = 10
# b = 20
#
# print(a + b)
#
# print(a ** b)
#
# print(b % a)
#
# print(b // a)

# age = 15
# print("if语句判断开始")
#
# if age > 18:
#     print("已成年")
# else:
#     print("未成年")
#
# print("if判断语句结束")


computer = random.randint(0,1)
print("请输入剪刀（0）、石头（1）、布（2）：")
computer2 = input()

computer2 = int(computer2)

if computer2 > computer:
    print("恭喜你，你赢了！")
else:
    print("哈哈，你输啦！")

