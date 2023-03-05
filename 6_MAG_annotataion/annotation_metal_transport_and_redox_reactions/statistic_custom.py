import os
dict_p={}
fr_p=open("bins_phylum.csv","r").read().splitlines()
for line_p in fr_p[1:]:
	i=line_p.split(",")[0]
	p=line_p.split(",")[1]
	dict_p[i]=p
dict_a={}
fr_a=open("abundance_average.csv","r").read().splitlines()
for line_a in fr_a[1:]:
	i=line_a.split(",")[0]
	a=line_a.split(",")[1]
	dict_a[i]=a

list1=os.listdir("./blastp_custom_result")
fw=open("statistic_custom_result.txt","w")
for file1 in list1:
	path1="./blastp_custom_result/" + file1
	fr1=open(path1,"r")
	lines1=fr1.read().splitlines()
	pre = ''
	for line1 in lines1:
		query = line1.split()[0]
		if query != pre:
			i=query.split("_")[0] + "_" + query.split("_")[1]
			gene=line1.split()[1]
			p=dict_p[i]
			a=dict_a[i]
			fw.write(i + "\t" + query + "\t" + gene + "\t" + p + "\t" + a + "\n")
			pre=query
