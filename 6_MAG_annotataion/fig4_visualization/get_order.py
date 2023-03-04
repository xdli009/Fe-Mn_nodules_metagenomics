fr_ns = open("ncyc_scyc_bin_table_melt_all.csv","r").read().splitlines()
dict_ns = {}
for line in fr_ns[1:]:
	phylum=line.split(",")[0]
	gene=line.split(",")[1]
	dict_ns.setdefault(gene,{})[phylum]=0
for line in fr_ns[1:]:
	phylum=line.split(",")[0]
	gene=line.split(",")[1]
	dict_ns[gene][phylum] = dict_ns[gene][phylum] + 1

fw_ns = open("ncyc_scyc_bin_table_melt_order_all.csv","w")
for gene in dict_ns.keys():
	for phylum in dict_ns[gene]:
		fw_ns.write(gene + "," + phylum + "," + str(dict_ns[gene][phylum]) + "\n")

