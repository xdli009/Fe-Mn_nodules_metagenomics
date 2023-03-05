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
dict_family={}
fr_family=open("./database_TCDB/families.py","r").read().splitlines()
for line_f in fr_family:
	i=line_f.split("\t")[0]
	a=line_f.split("\t")[1]
	dict_family[i]=a
list_family=[]
fr_list=open("metal_transporter_cluster_id.txt","r").read().splitlines()
for line_list in fr_list:
	list_family.append(line_list)

list1=os.listdir("blastp_TCDB_result")
fw=open("statistic_TCDB_result.txt","w")
for file1 in list1:
	path1="./blastp_TCDB_result/" + file1
	fr1=open(path1,"r")
	lines1=fr1.read().splitlines()
	pre = ''
	for line1 in lines1:
		query = line1.split()[0]
		if query != pre:
			i=query.split("_")[0] + "_" + query.split("_")[1]
			gene_5 = line1.split()[1].split("|")[3]
			gene=".".join(gene_5.split(".")[0:3])
			if gene in list_family:
				p=dict_p[i]
				a=dict_a[i]
				family=dict_family[gene]
				fw.write(i + "\t" + query + "\t" + gene + "\t" + p + "\t" + a + "\t" + gene_5 + "\t" + family + "\n")
			pre=query
