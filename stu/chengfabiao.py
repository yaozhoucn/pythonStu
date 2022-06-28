# -*- coding = utf-8 -*-
# @Time :2022/6/28 14:23
# @Author:HANG
# @File : chengfabiao.py
# @Software: PyCharm

# for i in range(1,10):
#     for j in range(1,10):
#         if i >= j:
#             print(i, "*", j, "=", i * j, end="\t")
#     print(" ")


i = 1
j = 1

while i <= 9:

    while j <= i:
        print(i, "*", j, "=", i * j, end="\t")
        j = j + 1
    i += 1
    j = 1
    print(" ")