# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:35:59 2020

@author: Donny
"""

import numpy as np

# #배열생성
# x = np.array([1.0, 2.0, 3.0])
# print(x)
# print(type(x))
# #-----------------------------#
# #산술연산
# y = np.array([2.0, 4.0, 6.0])
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

# print(x/2.0)
# #-----------------------------#
# #n차원 배열_2차원

# A = np.array([[1,2], [3,4]])
# print(A)
# print(A.shape)
# print(A.dtype)

# #n차원 배열 산술연산
# B = np.array([[3,0], [0,6]])
# print(A+B)
# print(A*B)

# #행렬x스칼라 연산
# print(A)
# print(A*10)

# #-----------------------------#
# #브로드캐스트

# A = np.array([[1,2], [3,4]])
# print(A.shape)
# C = np.array([10, 20])
# print(C.shape)
# print(A*C)

#-----------------------------#
#원소 접근
X = np.array([[51,55], [14,19],[0,4]])
print(X)
print(X.shape)

print(X[0])
print(X[0][1])

for row in X:
     print(row)
    

#인덱스를 배열로 지정하여 접근
X = X.flatten() #X를 1차원 배열로 변환(평탄화)
print(X)
print(X[np.array([0,2,4])]) #인덱스가 0, 2, 4인 원소 얻기

print(X>15)
print(X[X>15]) #값이 15 이상인 원소 출력 





















