import csv
import os
import re


def opencsv(filename):
	f = open(filename, 'r')
	reader = csv.reader(f)
	output = []
	for i in reader:
		output.append(i)
	return output
		

def writecsv(filename, the_list):
	with open(filename, 'w', newline='',encoding='utf-8-sig') as f:
		a = csv.writer(f, delimiter=',')
		a.writerows(the_list)


def switchStringToFloat(listname):
	for i in listname:
		for j in i:
			try:
				i[i.index(j)] = float(re.sub(',', '', j))
			except:
				pass
	return listname


