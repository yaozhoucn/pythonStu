# -*- coding = utf-8 -*-
# @Time :2022/6/28 11:30
# @Author:HANG
# @File : for_while_stu.py
# @Software: PyCharm

# 课堂练习：
# 1. 计算1~100的累积和（包含1和100）
# 2. 计算1~100之间偶数的累积和（包含1和100）

a = 0
sum = 0
# while a <= 100:
#
#     sum = sum + a
#     a = a + 1
#
# print(sum)

while a <= 100:
    if a % 2 == 0:
        sum = sum + a
    a = a + 1

print(sum)