fr_ns = open("../annotation_nitrogen_and_sulfur_metabolism/ncyc_scyc_eggnog_passed.txt","r").read().splitlines()
dict_ns = {}
dict_phylum = {}
all_gene = []
for line in fr_ns:
	gene = line.split()[0]
	binid = line.split()[2]
	phylum = line.split()[3]
	dict_phylum[binid] = phylum
	dict_ns.setdefault(binid,[]).append(gene)
	all_gene.append(gene)
fw_gene = open("ncyc_scyc_gene_table_all.txt","w")
fw_bin = open("ncyc_scyc_bin_table_all.txt","w")
fw_gene.write("bin" + "\t" + "phylum")
fw_bin.write("bin" + "\t" + "phylum")
list_gene = list(set(all_gene))
for gene in list_gene:
	fw_gene.write("\t" + gene)
	fw_bin.write("\t" + gene)
fw_gene.write("\n")
fw_bin.write("\n")
for binid in dict_ns.keys():
	phylum = dict_phylum[binid]
	fw_gene.write(binid + "\t" + phylum)
	fw_bin.write(binid + "\t" + phylum)
	for gene in list_gene:
		index_gene = 0
		index_bin = 0
		for i in dict_ns[binid]:
			if gene == i:
				index_gene = index_gene + 1
				index_bin = 1
		fw_gene.write("\t" + str(index_gene))
		fw_bin.write("\t" + str(index_bin))
	fw_gene.write("\n")
	fw_bin.write("\n")
