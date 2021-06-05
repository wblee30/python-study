
import pandas as pd

data = {
    'name' : ['Mark', 'Jane', 'Chris', 'Ryan'],
    'age' : [33, 32, 44, 42],
    'score' : [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)

print("++++++++++데이터 표시+++++++++++")
print("df : ", df)
print("++++++++++데이터 합계+++++++++++")
print("df.sum() : ", df.sum())
print("++++++++++데이터 평균+++++++++++")
print("df.mean() : ", df.mean())
print("++++++++++데이터 선택하기+++++++++++")
print("df.age : ", df.age)
print("df.['age'] : ", df['age'])