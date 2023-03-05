import os
dict_gene_N = {}
fr_gene_N = open("./database/id2gene.map.2019Jul","r").read().splitlines()
for line in fr_gene_N:
	l1=line.split()[0]
	l2=line.split()[1]
	dict_gene_N[l1]=l2
dict_gene_S = {}
fr_gene_S = open("./database/id2gene.map.2021","r").read().splitlines()
for line in fr_gene_S:
	l1=line.split()[0]
	l2=line.split()[1]
	dict_gene_S[l1]=l2
dict_p = {}
fr_p = open("../annotation_metal_transport_and_redox_reactions/bins_phylum.csv","r").read().splitlines()
for line in fr_p[1:]:
	l1=line.split(",")[0]
	l2=line.split(",")[1]
	dict_p[l1]=l2
dict_a = {}
fr_a = open("../annotation_metal_transport_and_redox_reactions/abundance_average.csv","r").read().splitlines()
for line_a in fr_a[1:]:
	i=line_a.split(",")[0]
	a=line_a.split(",")[1]
	dict_a[i]=a
dict_e={}
fr_e=open("./all.annotations","r").read().splitlines()
for line_e in fr_e:
	i=line_e.split()[0]
	dict_e[i]=line_e
fw_N = open("NCyc_eggnog_result.txt","w")
fw_S = open("SCyc_eggnog_result.txt","w")
list_m8 = os.listdir("./blastp_result/")
for m8 in list_m8:
	path_m8 = "./blastp_result/" + m8
	fr_m8 = open(path_m8,"r").read().splitlines()
	name=m8.split(".m8")[0]
	pre=""
	for line in fr_m8:
		l1=line.split()[0]
		if l1 != pre:
			l2=line.split()[1]
			l10=line.split()[10]
			if l2 in dict_gene_N.keys():
				gene=dict_gene_N[l2]
				gene_id = line.split()[1]
				bin_id = l1.split("_cg")[0]
				if l1 in dict_e.keys():
					eggnog = dict_e[l1]
				else:
					eggnog = "nona"
				abundance = dict_a[bin_id]
				phylum = dict_p[bin_id] 
				fw_N.write(l1 + "\t" + bin_id + "\t" + phylum + "\t" + abundance + "\t" + gene_id + "\t" + gene + "\t" + l10 + "\t" + eggnog + "\n")
				pre = l1
			elif l2 in dict_gene_S.keys():
				gene=dict_gene_S[l2]
				gene_id = line.split()[1]
				bin_id = l1.split("_cg")[0]
				if l1 in dict_e.keys():
					eggnog = dict_e[l1]
				else:
					eggnog = "nona"
				abundance = dict_a[bin_id]
				phylum = dict_p[bin_id]
				fw_S.write(l1 + "\t" + bin_id + "\t" + phylum + "\t" + abundance + "\t" + gene_id + "\t" + gene + "\t" + l10 + "\t" + eggnog + "\n")
				pre = l1
			else:
				print("none")
				pre = l1
