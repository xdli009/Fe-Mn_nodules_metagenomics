fr1 = open("bin_phylum_abundance_all_cycle_merge.txt","r").read().splitlines()
dict1 = {}
dict_abundance = {}
for line in fr1:
	gene = line.split()[0]
	bins = line.split()[1]
	phylum = line.split()[2]
	abundance = float(line.split()[3])
	dict_abundance[bins] = abundance
	dict1.setdefault(gene,[]).append(bins)
fr_high = open("../../4_figure_key_bins/abundance_n50/high_abundance_bin_id.txt","r").read().splitlines()
list_high = []
for line in fr_high:
	list_high.append(line)
fw = open("get_all_key.txt","w")
fw.write("Gene name" + "\t" + "The width of line represent abundance of dominant MAGs" + "\t" + "The width of line represent abundance of other MAGs" + "\t" + "Percentage of the abundance of dominant MAGs (%)" + "\t" + "Percentage of the abundance of other MAGs (%)" + "\n")
for gene in dict1.keys():
	list_bins = dict1[gene]
	a_all = float(0)
	a_high = float(0)
	for bins in list_bins:
		if bins in list_high:
			a_high = a_high + dict_abundance[bins]
		else:
			a_all = a_all + dict_abundance[bins]
	a = a_high + a_all
	l_a_all = a_all/10
	l_a_high = a_high/10
	l_a = a/10
	per_a_all = l_a_all/l_a*100
	per_a_high = l_a_high/l_a*100
	fw.write(gene + "\t" + str(l_a_high) + "\t" + str(l_a_all) + "\t" + str(l_a) + "\t" + str(per_a_high) + "\t" + str(per_a_all) + "\n")
