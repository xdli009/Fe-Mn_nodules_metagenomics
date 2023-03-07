import os
 
dict_id = {}
fr_id = open("/beegfs/home/lxd/2_sea_metagenomics/6.metabat2/bins_redup_refinem_drep/derep_70_10/6_nr_check/nr_id.txt","r").read().splitlines() #All identifiers of NR's fasta file,such as '>MPT15656.1 ABC transporter permease [Microbacterium sp.]'
for line in fr_id:
	l_id = line.split(">")[1].split()[0]
	l_id_split = l_id + " "
	l_anno = line.split(l_id_split)[1].split(" [")[0]
	dict_id[l_id] = l_anno

fw = open("all_anno_to_nr.txt","w")
fr1 = open("all_anno.txt","r").read().splitlines()
list1 = []
for bln in os.listdir("./all_proteins_annotated"):
	if ".bln" in bln:
		list1.append(bln.split(".bln")[0])

for line in fr1[1:]:
	genes = line.split()[0]
	bins = genes.split("_cg")[0]
	name = line.split()[1]
	if genes in list1:
		path_nr = "./all_proteins_annotated/" + genes + ".bln"
		fr_nr = open(path_nr,"r").read().splitlines()
		nr_gene_id = fr_nr[0].split()[1]
		nr_anno = dict_id[nr_gene_id]
		identity = fr_nr[0].split()[2]
		list_anno = []
		for line_nr in fr_nr:
			nr_gene_id = line_nr.split()[1]
			nr_anno_other = dict_id[nr_gene_id]
			list_anno.append(nr_anno_other)
		str_anno = ",".join(list_anno[1:21])
		fw.write(genes + "\t" + name + "\t" + nr_anno + "\t" + identity + "\t" + str_anno + "\n")
	else:
		fw.write(genes + "\t" + name + "\t" + "without annotation" + "\n")
