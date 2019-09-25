import csv
import os

def csvRead(File_Name):
	with open(File_Name,'r',newline='') as writeFile:
		data = list(csv.reader(writeFile))
		return data


def csvWrite(File_Name,array):
	with open(File_Name, 'w', newline='') as writeFile:
		writer = csv.writer(writeFile, lineterminator='\n')
		writer.writerows(array)

def csvAppend(File_Name,record):
	with open(File_Name, 'a', newline='') as writeFile:
		writer = csv.writer(writeFile, lineterminator='\n')
		writer.writerows(record)	
