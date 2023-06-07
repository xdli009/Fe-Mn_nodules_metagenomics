fr_ns = open("simple_compounds_ko_id_phylum_redup.txt","r").read().splitlines()
dict_ns = {}
for line in fr_ns:
	phylum=line.split()[0]
	gene=line.split()[1]
	dict_ns.setdefault(gene,{})[phylum]=0
for line in fr_ns:
	phylum=line.split()[0]
	gene=line.split()[1]
	dict_ns[gene][phylum] = dict_ns[gene][phylum] + 1

fw_ns = open("simple_compounds_ko_id_phylum_redup_order.csv","w")
for gene in dict_ns.keys():
	for phylum in dict_ns[gene]:
		fw_ns.write(gene + "," + phylum + "," + str(dict_ns[gene][phylum]) + "\n")

