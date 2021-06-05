# ex1: Monica 대사 슬라이싱

import os, re, codecs

print("**********************ex1*******************")

# manuscript 저장 경로 불러오기
os.chdir(r'C:\Users\wblee\PycharmProjects\study\manuscript')

# 파일 열기 함수 및 객체 생성
f = codecs.open('friend101.txt', 'r', encoding = 'utf-8')

# 객체 생성 및 파일 읽기
script101 = f.read()
print("script101[:100]:",script101[:100])

# 모니카를 포함하는 내용 슬라이싱
Line = re.findall(r'Monica:.+', script101)

print("Line:", Line[:3])

for item in Line[:3]:
	print(item)

# 파일 닫기
f.close()

# monica.txt. 파일 열기 및 쓰기 형태로 파일 열기
f = codecs.open('monica.txt', 'w', encoding = 'utf-8')

# monica string 변수 생성
monica = ''

for i in Line:
	monica += i

# 내용 쓰기
f.write(monica)

# 파일 닫기
f.close()

print("**********************ex2*******************")

char = re.compile(r'[A-Z][a-z]+:')
people_tmp = set(re.findall(char, script101))
people = list(people_tmp)
character = []
for i in people:
	character += [i[:-1]]

# 위의 6줄의 코드를 한줄로 표현하기
# character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+: ', script101)))]
print("character:", character)

print("**********************ex3*******************")

Jimun_slicing = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)
print(Jimun_slicing[:6])

print("**********************ex4*******************")

f = open('friend101.txt','r')
f.read(100)
f.seek(0)

sentences = f.readlines()
print("sentences[:3]:",sentences[:3])

for i in sentences[:20]:
	if re.match(r'[A-Z][a-z]+:', i):
		print(i)

figure_speech = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i)]
print("figure_speech[:10]:", figure_speech[:10])

would = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('would',i)]
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('take',i)]

for i in take:
	print(i)

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()