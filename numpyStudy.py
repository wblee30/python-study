
import numpy as np


print("+++++++++++++++++++++++++numpy 배열 선언+++++++++++++++++++++++++")
a = np.array([[2,3], [5,2]])
print("a:", a)

d = np.array([[1,2,3,4,5], [2,4,5,6,7], [5,7,8,9,9]])
print("d:", d)

print("+++++++++++++++++++++++++numpy Slice+++++++++++++++++++++++++")
print("d[1][2] :", d[1][2], "d[1, 2] :", d[1, 2], "d[1:, 3:] :", d[1:, 3:])

print("+++++++++++++++++++++++++배열 크기 알아보기: shape+++++++++++++++++++++++++")
print("d.shape : ", d.shape)

print("+++++++++++++++++++++++++배열 자료형 알아보기: dtype+++++++++++++++++++++++++")
print("d.dtype : ", d.dtype)

print("+++++++++++++++++++++++++배열 자료형 바꾸기: astype()+++++++++++++++++++++++++")
print("d.astype : ", d.astype('float64'))
print("d.dtype : ", d.dtype)

print("+++++++++++++++++++++++++0으로 이루어진 배열 만들기: np.zeros()+++++++++++++++++++++++++")
zero = np.zeros((2,10))
print("zeroes : ", zero)

print("+++++++++++++++++++++++++1으로 이루어진 배열 만들기: np.ones()+++++++++++++++++++++++++")
one = np.ones((2,10))
print("zeroes : ", one)

print("+++++++++++++++++++++++++연속형 정수 생성하기: np.arange(2,10) - 2이상 10 미만+++++++++++++++++++++++++")
arange = np.arange(2,10)
print("zeroes : ", arange)

print("+++++++++++++++++++++++++전치 행렬 만들기: np.transpose()+++++++++++++++++++++++++")
dTrans = np.transpose(d)
print("dTrans : ", dTrans)
