fr1 = open("./high_abundance_bin_id.txt","r").read().splitlines()
list_id1 = []
for line in fr1:
	list_id1.append(line)
fr2 = open("../6_MAG_annotataion/annotation_CAZymes/statistic_bins_CAZy_MAGs_info_list.txt","r").read().splitlines()
fw = open("high_bin_cazy_phylum_abundance_passed.txt","w")
for line in fr2:
	id2 = line.split()[0]
	if id2 in list_id1:
		l1 = line.split()[1]
		l2 = line.split()[2]
		l3 = line.split()[3]
		fw.write(id2 + "\t" + "-" + "\t" + l3 + "\t" + l3 + "\t" + l1 + "\t" + l2 + "\n")
