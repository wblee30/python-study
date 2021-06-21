
import os
import re
from library import usecsv
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

df2 = pd.read_csv('./manuscript/survey.csv')
print("df2.shape:", df2.shape)
print("df2.info", df2.info())
#male = df2.income[df2.sex == 'm']
#female = df2.income[df2.sex == 'f']
#stats.ttest_ind(male,female)

# print("+++++++++평균과 합 구하기++++++++++")
# print("df2.head() : ", df2.head())
# print("df2.mean() : ", df2.mean())
# print("df2.income.mean() : ", df2.income.mean())
# print("df2.income.sum() : ", df2.income.sum())
#
# print("+++++++++중앙값 구하기++++++++++")
# print("df2.income.median() : ", df2.income.median())
#
# print("+++++++++기초통계량 요약해서 출력하기++++++++++")
# print("df2.describe() : ", df2.describe())
# print("df2.income.describe() : ", df2.income.describe())
#
# print("df2.sex.value_counts() : ", df2.sex.value_counts())
# print("df2.groupby(df2.sex).mean()", df2.groupby(df2.sex).mean())

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

ttest_result = stats.ttest_ind(male, female)
print(ttest_result)

print("ttest_result[0]", ttest_result[0])
print("ttest_result[1]", ttest_result[1])

if ttest_result[1] > 0.05:
    print(f'p-value는 {ttest_result[1]}로 95% 수준에서 유의하지않음')
else:
    print(f'p-value는 {ttest_result[1]}로 95% 수준에서 유의함')

corr = df2.corr(method= 'spearman')
print("corr:", corr)

income_stress_corr = df2.income.corr(df2.stress)
print("income_stress_corr:", income_stress_corr)

corr.to_csv('corr.csv')

model = smf.ols(formula='jobSatisfaction~English', data=df2)
result = model.fit()
print("summary",result.summary())