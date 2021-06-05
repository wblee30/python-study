
import os
import re
from library import usecsv
import pandas as pd
#from scipy import stats


os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

df2 = pd.read_csv('survey.csv')

#male = df2.income[df2.sex == 'm']
#female = df2.income[df2.sex == 'f']
#stats.ttest_ind(male,female)

print("+++++++++평균과 합 구하기++++++++++")
print("df2.head() : ", df2.head())
print("df2.mean() : ", df2.mean())
print("df2.income.mean() : ", df2.income.mean())
print("df2.income.sum() : ", df2.income.sum())

print("+++++++++중앙값 구하기++++++++++")
print("df2.income.median() : ", df2.income.median())

print("+++++++++기초통계량 요약해서 출력하기++++++++++")
print("df2.describe() : ", df2.describe())
print("df2.income.describe() : ", df2.income.describe())

print("df2.sex.value_counts() : ", df2.sex.value_counts())
print("df2.groupby(df2.sex).mean()", df2.groupby(df2.sex).mean())

