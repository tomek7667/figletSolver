from pwn import *
from pyfiglet import Figlet
import string
candidates = ';:"'+"'-"+string.ascii_lowercase+string.ascii_uppercase+"?"+"."+"!"+","
figlet = Figlet()
def size(str):
	size = 0;
	for i in range(6):
			size += len(str[i])
	return size

def findString(allMatches, found, searchingFor, sensitivity):
	values = []
	hadPerfetMatch = False;
	for candidate in candidates:
		case = figlet.renderText(found + candidate)
		case = case.split("\n")
		matches = 0
		if(size(case) > size(searchingFor)):
			continue;
		perfectMatch = True
		for i in range(6):
			for j in range(len(case[i])-sensitivity):
				if(case[i][j] != searchingFor[i][j]):
					perfectMatch = False
		
		if(size(searchingFor) == size(case) and perfectMatch):
			matches = True;
			for i in range(6):
				for j in range(len(case[i])):
					if(case[i][j] != searchingFor[i][j]):
						matches = False;
			   
			if matches:
				return found + candidate;
		
		if(perfectMatch):
			hadPerfetMatch = True;
			values.append(findString(matches, found+candidate, searchingFor, sensitivity))
	if not (hadPerfetMatch):
		return
	else:
		for value in values:
			if value != None:
				return value;
r = remote("tirefire.org", 11051)
counter = 0
jd = r.recv().split(b"\n")[2:]
[str(i) for i in jd]
[i[2:] for i in jd]
[i[:-1] for i in jd]
for i in jd:
	print(i)
jd = jd[:-1]
for i in range(len(jd)):
	jd[i] = jd[i].decode("utf-8")

first = findString(0, "", jd, 3)
r.sendline(first)
counter +=1
while True:
	jd = r.recv().split(b"\n")
	
	[str(i) for i in jd]
	[i[2:] for i in jd]
	[i[:-1] for i in jd]
	jd = jd[:-1]
	for i in range(len(jd)):
		jd[i] = jd[i].decode("utf-8")
	print("Slowo: ", counter)
	for i in jd:
		print(i)
	first = findString(0, "", jd, 2)
	if first == None:
		first = findString(0, "", jd, 3)
	
	r.sendline(first)
	counter+=1
