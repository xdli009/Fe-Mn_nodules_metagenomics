import random
fr1 = open("low_abundance_bin_id.txt","r").read().splitlines()
sample_num = 18
dict_random = {}
for i in range(0,100):
	dict_random[i] = random.sample(fr1,sample_num)
fr_tcdb = open("metal_transport_proteins.txt","r").read().splitlines()
fr_redox = open("metal_redox_proteins.txt","r").read().splitlines()
fr_ncyc = open("ncyc_proteins.txt","r").read().splitlines()
fr_scyc = open("scyc_proteins.txt","r").read().splitlines()
fr_cazy = open("CAZy_proteins.txt","r").read().splitlines()
fw = open("low_bin_profile_all.txt","w")
for i in dict_random.keys():
	list_id = dict_random[i]
	list_tcdb = []
	for line in fr_tcdb:
		id_mag = line.split()[0]
		if id_mag in list_id:
			gene = line.split()[3]
			list_tcdb.append(gene)
	num_tcdb = len(set(list_tcdb))
	fw.write(str(num_tcdb) + "\t" + "transport" + "\n")
for i in dict_random.keys():
	list_id = dict_random[i]
	list_redox = []
	for line in fr_redox:
		id_mag = line.split()[0]
		if id_mag in list_id:
			gene = line.split()[3]
			list_redox.append(gene)
	num_redox = len(set(list_redox))
	fw.write(str(num_redox) + "\t" + "redox" + "\n")
for i in dict_random.keys():
	list_id = dict_random[i]
	list_ncyc = []
	for line in fr_ncyc:
		id_mag = line.split()[2]
		if id_mag in list_id:
			gene = line.split()[0]
			list_ncyc.append(gene)
	num_ncyc = len(set(list_ncyc))
	fw.write(str(num_ncyc) + "\t" + "ncyc" + "\n")
for i in dict_random.keys():
	list_id = dict_random[i]
	list_scyc = []
	for line in fr_scyc:
		id_mag = line.split()[2]
		if id_mag in list_id:
			gene = line.split()[0]
			list_scyc.append(gene)
	num_scyc = len(set(list_scyc))
	fw.write(str(num_scyc) + "\t" + "scyc" + "\n")
for i in dict_random.keys():
	list_id = dict_random[i]
	list_cazy = []
	for line in fr_cazy:
		id_mag = line.split()[0]
		if id_mag in list_id:
			gene = line.split()[3]
			list_cazy.append(gene)
	num_cazy = len(set(list_cazy))
	fw.write(str(num_cazy) + "\t" + "cazy" + "\n")

