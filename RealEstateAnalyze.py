import os
import re
from library import usecsv

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')
apt = usecsv.switchStringToFloat(usecsv.opencsv('apt_202012.csv'))

print("apt[:3]", apt[:3])
print(len((apt)))

print("+++++++전체 정보 출력하기+++++++")
for i in apt[:6]:
    print(i)

print("+++++++시군구만 출력하기+++++++")
for i in apt[:6]:
    print(i[0])

print("+++++++시군구, 단지명, 거래대금 출력하기+++++++")
for i in apt[:6]:
    print(i[0], i[4], i[-4])

print("+++++++120m2 이상 3억원 이하 아파트 출력하기+++++++")
newList = []

for i in apt:
    try:
        # 오류가 날 경우를 대비해 예외 처리 사용
        if i[5] > 120 and i[-4] < 30000 and re.match('강원', i[0]):
            # 강원지역에 면적 120m2 이상, 시세 3억원 이하인 아파트 출력
            # append 사용 시, list 형태 []를 주의하여 사용할 것
            newList.append([i[0], i[4], i[-4]])
            # print(i[0], i[4], i[-4])
    except:
        pass

usecsv.writecsv('over120_lower30000_in_gangwon.csv', newList)

