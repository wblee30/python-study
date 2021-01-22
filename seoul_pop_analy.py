from library import usecsv
import os
import re

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)

# i = newPop[1]
# foreign = round(i[2] / (i[1]+i[2]) *100, 1)
#

# new.append([i[0], i[1], i[2], foreign])
#
# print("new:", new)

new = [['구', '한국인', '외국인', '외국인 비율(%)']]

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1]+i[2]) *100, 1)
        if foreign > 3:
            new.append([i[0],i[1],i[2], foreign])
    except:
        pass

usecsv.writecsv('newPop.csv', new)
print("new:", new)