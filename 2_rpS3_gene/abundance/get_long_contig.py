import os
from Bio import SeqIO
fr_phylum = open("../classification/rpS3_phylum.txt","r").read().splitlines()
list_centroid = []
dict_phylum = {}
for line in fr_phylum:
	rps3_id = line.split("\t")[0]
	phylum = line.split("\t")[1]
	list_centroid.append(rps3_id)
	dict_phylum[rps3_id] = phylum
list_cluster = os.listdir("../cluster_dir")
dict_contig_sample = {}
dict_contig = {}
list_contig = os.listdir("../rpS3_fasta")
for contigs in list_contig:
	if "_rpS3.fasta" in contigs:
		rps3_path = "../rpS3_fasta/" + contigs
		rps3_fa = SeqIO.parse(rps3_path,"fasta")
		name = contigs.split("_rpS3")[0]
		contigs_path = "../../1_metagenomics_assembly/pullseq_result/" + name + "_1000bp.fasta"
		contigs_fa = SeqIO.to_dict(SeqIO.parse(contigs_path,"fasta"))
		for rps3 in rps3_fa:
			rps3_id = rps3.id
			contig_id = rps3_id.rsplit("_",1)[0]
			dict_contig.setdefault(name,{})[contig_id] = contigs_fa[contig_id]
			dict_contig_sample[rps3_id] = name
		print(len(dict_contig[name].keys()))	
list_fa = []
list_fa_id = []
fw_info = open("long_contig_info.txt","w")
fw_map = open("all_rps3_to_contig_id.txt","w")
for cluster in list_cluster:
	path = "../cluster_dir/" + cluster
	fas = SeqIO.parse(path,"fasta")
	for fa in fas:
		rps3_id = fa.id
		if rps3_id in list_centroid:
			phylum = dict_phylum[rps3_id]
			centroid = rps3_id
	fas = SeqIO.parse(path,"fasta")
	pre_len = 0
	for fa in fas:
		rps3_id = fa.id
		contig_id = rps3_id.rsplit("_",1)[0]
		sample = dict_contig_sample[rps3_id]
		length = len(dict_contig[sample][contig_id].seq)
		contig_name = sample + "__" + contig_id
		fw_map.write(rps3_id + "\t" + contig_name + "\n")
		if length > pre_len:
			pre = contig_id
			pre_sample = sample
			pre_len = length
	name = pre_sample + "__" + pre
	if name not in list_fa_id:
		dict_contig[pre_sample][pre].id = name
		list_fa.append(dict_contig[pre_sample][pre])
		list_fa_id.append(name)
	fw_info.write(centroid + "\t" + phylum + "\t" + pre + "\t" + name + "\t" + str(pre_len) + "\n")
SeqIO.write(list_fa,"long_contig.fasta","fasta")
