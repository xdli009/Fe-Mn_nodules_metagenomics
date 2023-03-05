import os
listdir=os.listdir("./dom_tbl")
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

fw1=open("statistic_bins_CAZy.csv","w")
for i in typelist1:
	fw1.write("," + i)
fw1.write("\n")
for key2 in dict1.keys():
	fw1.write(key2)
	for i in typelist1:
		if i in dict1[key2]:
			fw1.write("," + "1")
		else:
			fw1.write("," + "0")
	fw1.write("\n")
fw1.close()
