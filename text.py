from library import usecsv
from library.usecsv import *

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')
b = [['국어','영어','수학'], [99,98,77]]
usecsv.writecsv('test.csv',b)