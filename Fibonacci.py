import numpy as np


def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')),
                  i) * np.matrix([[1], [0]])
        print(int(res[0][0]))


fib_matrix(50)


def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    return np.linalg.matrix_power(Matrix, n)


def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list


Fibonacci_Matrix(300)
