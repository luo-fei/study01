#!/usr/bin/env python3
# _*_  coding: utf-8 _*_

def triangle():
    line = [1]         # 第一行就一个元素1
    while True:
        yield line
        # 生成下一行，表达式为 : [1] + 上一行的两个元素之和 + [1]
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]


n = 0     # 控制输出行数
for item in triangle():
    print(item)
    n += 1
    if n % 10 == 0:
        break

