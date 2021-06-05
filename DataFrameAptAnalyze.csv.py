

import os
import re
from library import usecsv
import pandas as pd


os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

df = pd.read_csv('apt.csv', encoding='cp949')

print("++++++++++++++++처음이나 마지막 자료 일부만 출력하기++++++++++++++++++")
print('len(df) : ', len(df))
print('df.head() : ', df.head())
print('df.tail() : ', df.tail())

print("++++++++++++++++열 전체로 출력하기++++++++++++++++++")
print('df.지역 : ', df.지역)

print("++++++++++++++++조건별로 출력하기++++++++++++++++++")
print('df[df.면적 > 130] : ', df[df.면적 > 130])
print('df.가격[df.면적 > 130] : ', df.가격[df.면적 > 130])
print('df.가격[(df.면적 > 130) & (df.가격 < 15000)] : ', df.가격[(df.면적 > 130) & (df.가격 < 15000)])
print('df.가격[(df.면적 > 130) | (df.가격 < 15000)] : ', df.가격[(df.면적 > 130) | (df.가격 < 15000)])

print("++++++++++++++++원하는 자료만 살펴보기++++++++++++++++++")
print("df.loc[:10, ['아파트', '가격']] : ", df.loc[:10, ['아파트', '가격']])
print("df.loc[:, ['아파트', '가격']][df.가격 > 40000] : ", df.loc[:, ['아파트', '가격']][df.가격 > 40000])

print("++++++++++++++++데이터 추가하기++++++++++++++++++")
df['평 단가'] = df.가격/ df.면적
print("df.loc[:10, ('가격', '면적', '평 단가')] : ", df.loc[:10, ('가격', '면적', '평 단가')])

print("++++++++++++++++데이터 정렬하기++++++++++++++++++")
print("df.sort_values(by = '가격').loc[:, ['가격', '지역']] : ", df.sort_values(by = '가격').loc[:, ['가격', '지역']])
print("df.sort_values(by = '가격', ascending = False).loc[:, ['가격', '지역']] : ", df.sort_values(by = '가격', ascending = False).loc[:, ['가격', '지역']])
print("df[df.가격 > 40000].sort_values(by = '면적').loc('가격','면적','지역') : " , df[df.가격 > 40000].sort_values(by = '면적').loc[:, ('가격','면적','지역')])

print("++++++++++++++++문자열 다루기++++++++++++++++++")
print("df.지역.str.find('강릉') : ", df.지역.str.find('강릉'))
print("df[df.지역.str.find('강릉') > -1] : ", df[df.지역.str.find('강릉') > -1])
dfF = df[df.지역.str.find('강릉') > -1]
print("dfF.mean() : ", dfF.mean())


print("++++++++++데이터프레임에서 Comma 제거 기능 사용하기++++++++++")
os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

df = pd.read_csv('apt_comma.csv', encoding='cp949')
df.가격 = df.가격.str.replace(',','').astype('int64')
print("df.가격 : ",df.가격)
print("df.가격 > 40000 : ", df[df.가격 > 40000])

