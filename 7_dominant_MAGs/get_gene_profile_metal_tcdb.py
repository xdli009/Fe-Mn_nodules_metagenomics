fr1 = open("./high_abundance_bin_id.txt","r").read().splitlines()
list_id1 = []
for line in fr1:
	list_id1.append(line)
fr2 = open("../6_MAG_annotataion/annotation_metal_transport_and_redox_reactions/NR_check/bin_mental_tcdb_phylum_abundance_passed.txt","r").read().splitlines()
fw = open("high_bin_mental_tcdb_phylum_abundance_passed.txt","w")
for line in fr2:
	id2 = line.split()[0]
	if id2 in list_id1:
		fw.write(line + "\n")
