
import re, os
from library import usecsv

English = 'She is a vegeterian. She does not eat meat. She thinks that animals should not be killed.' \
          'It is hard for her to hang out with people. Many people like to eat meat. She told his parents' \
          'not to have meat. They laughed at her. She realized they couldn\'t give up meat.'

Korean = '그녀는 채식주의 자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽여서는 안된다고 생각합니다. 사람들과 어울리는 것이 그녀에게 어렵습니다.' \
         ' 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었습니다.' \
         ' 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'

os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

KoreanList = re.split('\.', Korean)
EnglishList = re.split('\.', English)

print(EnglishList)
print(KoreanList)

total = []

for i in range(len(EnglishList)):
    total.append([EnglishList[i], KoreanList[i]])
    
usecsv.writecsv('Korean_English.csv', total)