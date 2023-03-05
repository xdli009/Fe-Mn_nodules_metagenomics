from Bio import SeqIO
faa_list = []
fr_nc = open("id2gene.map.2019Jul","r").read().splitlines()
list_nc = []
for line in fr_nc:
	id0 = line.split()[0]
	list_nc.append(id0)
nc = SeqIO.parse("NCyc_100_2019Jul.faa","fasta")
for faa in nc:
	id_faa = faa.id
	if id_faa in list_nc:
		faa_list.append(faa)	
fr_sc = open("id2gene.map.2021","r").read().splitlines()
list_sc = []
for line in fr_sc:
	id0 = line.split()[0]
	list_sc.append(id0)
sc = SeqIO.parse("SCycDB_2020Mar.faa","fasta")
for faa in sc:
	id_faa = faa.id
	if id_faa in list_sc:
		faa_list.append(faa)
SeqIO.write(faa_list,"ncyc_scyc_db.faa","fasta")

