fr1 = open("/beegfs/home/lxd/2_sea_metagenomics/6.metabat2/bins_redup_refinem_drep/derep_70_10/derepbins_ncyc_scyc/blastp/m8_eggnog/bins_phylum.csv","r").read().splitlines()
dict1 = {}
for line in fr1[1:]:
	l1 = line.split(",")[0]
	l2 = line.split(",")[1]
	dict1[l1] =l2
fr2 = open("simple_compounds_ko_id_phylum.txt","r").read().splitlines()
fw = open("matrix_simple_compounds_ko.txt","w")
dict2 = {}
list_gene = []
for line in fr2:
	bin_id = line.split()[3]
	gene = line.split()[0]
	dict2.setdefault(bin_id,[]).append(gene)
	list_gene.append(gene)
list_gene = list(set(list_gene))
fw.write("MAGs ID" + "\t" + "MAG's classification at the phylum level")
for gene in list_gene:
	fw.write("\t" + gene)
fw.write("\n")
for bin_id in dict1.keys():
	fw.write(bin_id)
	phylum = dict1[bin_id]
	fw.write("\t" + phylum)
	for gene in list_gene:
		if bin_id in dict2.keys():
			if gene in dict2[bin_id]:
				fw.write("\t" + "1")
			else:
				fw.write("\t" + "0")
		else:
			fw.write("\t" + "0")
	fw.write("\n")
