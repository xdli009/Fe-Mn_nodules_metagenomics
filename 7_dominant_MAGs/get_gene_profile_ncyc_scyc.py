fr1 = open("./high_abundance_bin_id.txt","r").read().splitlines()
list_id1 = []
for line in fr1:
	list_id1.append(line)
fr2 = open("../6_MAG_annotataion/annotation_nitrogen_and_sulfur_metabolism/ncyc_scyc_eggnog_passed.txt","r").read().splitlines()
fw = open("high_bin_nitrogen_sulfur_phylum_abundance_passed.txt","w")
for line in fr2:
	id2 = line.split()[2]
	if id2 in list_id1:
		l0 = line.split()[0]
		l1 = line.split()[1]
		l3 = line.split()[3]
		l4 = line.split()[4]
		fw.write(id2 + "\t" + l1 + "\t" + l0 + "\t" + l0 + "\t" + l3 + "\t" + l4 + "\n")
