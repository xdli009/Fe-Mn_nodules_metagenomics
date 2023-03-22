pass_id = open("check_passed_id.txt","r").read().splitlines()
gene_info = open("bin_mental_tcdb_phylum_abundance.txt","r").read().splitlines()
fw = open("bin_mental_tcdb_phylum_abundance_passed.txt","w")
fw.write(gene_info[0] + "\n")
for line in gene_info[1:]:
	gene_id = line.split()[1]
	if gene_id in pass_id:
		fw.write(line + "\n")
