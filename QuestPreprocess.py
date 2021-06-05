from library import usecsv
import numpy as np
import os, re

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

quest = np.array(usecsv.switchStringToFloat(usecsv.opencsv('quest.csv')))

print(quest > 5)
print(quest[quest > 5])

quest[quest > 5] = 5
print(quest)

usecsv.writecsv('questResult.csv', list(quest))
