from library.usecsv import *
from library import usecsv


print('***************************ex1***************************')

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

f = open('a.csv', 'r', encoding='utf-8')
new = csv.reader(f)
a_list = []
for i in new:
    print(i)
    a_list.append(i)

print('***************************ex2***************************')
a = [['구' , '전체' , '내국인' , '외국인'],
     ['관악구' , '519864' , '502089' , '17775'],
     ['강남구' , '547602' , '542498' , '5104'],
     ['송파구' , '686181' , '679247' , '6934'],
     ['강동구' , '428547' , '424235' , '4312']]

f = open('temp.csv', 'w', newline='', encoding='utf-8')
csvobject = csv.writer(f, delimiter = ',')
csvobject.writerows(a)
f.close()

b = [['국어','영어','수학'], [99,98,77]]
usecsv.writecsv('test.csv',b)



