import os
fr2=open("phylum.txt","r")
lines2=fr2.read().splitlines()
dict2={}
for line2 in lines2[1:]:
	key2=line2.split()[1]
	value2= line2.split()[0]
	dict2.setdefault(key2,[]).append(value2)

listdir=os.listdir("./dom_tbl/")
dict1={}
for file1 in listdir:
	path1="./dom_tbl/" + file1
	fr1=open(path1,"r")
	lines1=fr1.readlines()
	name=file1.split("_dom")[0]
	pre=''
	for line1 in lines1:
		if line1.startswith("#")==False:
			id1=line1.split()[3]
			if not id1 == pre:
				str1=line1.split()[0].split(".")[0].split("_")[0]
				dict1.setdefault(name,[]).append(str1)
				pre=id1
	fr1.close()
typelist=[]
for key1 in dict1.keys():
	typelist.extend(dict1[key1])
typelist=list(set(typelist))
typelist1=[]
for a in typelist:
	if "CE" in a or "GH" in a or "PL" in a:
		typelist1.append(a) 
typelist1.sort()

fw1=open("statistic_phylum_CAZy.csv","w")
for i in typelist1:
	fw1.write("," + i)
fw1.write("\n")
for key2 in dict2.keys():
	length=len(dict2[key2])
	fw1.write(key2 + "(" + str(length) + ")")
	for i in typelist1:
		num=int(0)
		for j in dict2[key2]:
			if i in dict1[j]:
				num=num+1
		percent=num/length
		fw1.write("," + str(percent))
	fw1.write("\n")
fw1.close()
