import os
import re
from library import usecsv

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')
apt = usecsv.switch(usecsv.opencsv('apt_202012.csv'))

print("apt[:3]", apt[:3])

print(len((apt)))