#!/usr/bin/env python3
# _*_  coding: utf-8 _*_


n = int(input('请输入三角形的高度：'))  # 目标层数

layer = 1  # 当前层数为 1
values = [1]  # 当前层的内容

while layer <= n:  # 当 现在的层数 <= 目标层数 时：
    new_values = [1]  # 下一层的内容
    index = 0  # 编号初始化为 0

    # 打印和创建层
    while index < len(values):  # len(values) 为values列表内元素的个数 #当 编号<=values内元素的个数时：
        print('%d.' % values[index], end='')  # 打印 values[index] , 循环结束即为打印 values内的所有元素
        if (index < layer - 1):
            new_values.append(values[index] + values[index + 1])
        index += 1

    new_values.append(1)
    values = new_values  # 下一层内容替换当前层内容
    print('')
    layer += 1
