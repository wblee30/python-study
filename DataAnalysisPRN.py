import os
import pandas as pd
from library import usecsv
import re

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

df = pd.read_csv('PRN_Jan.csv')
df2 = pd.read_csv('newData.csv')

print("len(df) : ", len(df))
print(df.info())
print("df.columns :", df.columns)
print("df.head() :", df.head())
print(df.품목코드.value_counts())
print(df.품목코드.value_counts().sum())
print(df2.품목코드.value_counts())
print(df2.품목코드.value_counts().sum())

print(df[df.품목코드 == "FNSC"].loc[:, ('NO', '처방일', '병동', '진료과', '등록번호', '환자명', '품목명', '품목코드')])
print(df.iloc[1, 9])
print(df.loc[[1, ]])

code = ["ASPSY", "ATN", "AHCPA", "NCCD1", "STDMA", "AMBSY"
    , "F50DWA", "AHDR", "XTFT", "NCFTT", "NCFTT2", "DULXA"
    , "APHLA", "AIBV", "BAV-SL", "KT7-PT", "AKCA", "HT5BTA"
    , "MTDFEP", "TR1/2AVA", "TRAVA", "ULMG", "BCOPC", "GDMPA", "NCMOA"
    , "NC1/2MOA", "HTPDA", "CNG", "AH1/2ODA", "AHODA", "NCIC", "DTPZ"
    , "NC1/2DMA", "NCDMA", "AREA", "ADOV", "AP1/2QP", "AP1QT", "VT-SL"
    , "FNSC", "ASTPA", "ATRA", "A1/2US", "ADTT", "SO1/2ZP", "SOZP", "SO1/2SC"]


# newList = []
# for i in code:
#     for j in range(14142):
#         if df.iloc[j, 9] == i:
#             newList.append(df.loc[j, ])

# usecsv.writecsv('newData.csv', newList)
