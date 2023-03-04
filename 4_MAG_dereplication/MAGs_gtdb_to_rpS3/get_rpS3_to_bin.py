import os
from Bio import SeqIO
fr_phylum = open("all_rps3_relative_abundance_average_to_info.txt","r").read().splitlines()
list_centroid = []
dict_phylum = {}
for line in fr_phylum:
	rps3_id = line.split("\t")[0]
	contig_id = line.split("\t")[4]
	list_centroid.append(rps3_id)
	dict_phylum[rps3_id] = line
list_cluster = os.listdir("../../2_rpS3_gene/cluster_dir")
dict_phylum_a = {}
dict_rps3_to_centroid = {}
for cluster in list_cluster:
	path = "../../2_rpS3_gene/cluster_dir/" + cluster
	fas = SeqIO.parse(path,"fasta")
	for fa in fas:
		rps3_id = fa.id
		if rps3_id in list_centroid:
			phylum = dict_phylum[rps3_id]
			centroid = rps3_id
	fas = SeqIO.parse(path,"fasta")
	for fa in fas:
		rps3_id = fa.id
		dict_phylum_a[rps3_id] = phylum
		dict_rps3_to_centroid[rps3_id] = centroid
#rps3 map to contig
fr_map = open("../../2_rpS3_gene/abundance/all_rps3_to_contig_id.txt","r").read().splitlines()
dict_map = {}
for line in fr_map:
	rps3 = line.split()[0]
	contig = line.split()[1]
	dict_map[contig] = rps3
#get bin contig id to rpS3
fr_bin_phylum = open("bins_phylum.csv","r").read().splitlines()
dict_bin_phylum = {}
for line in fr_bin_phylum[1:]:
	line_bin = line.split(",")[0]
	line_phylum = line.split(",")[1]
	dict_bin_phylum[line_bin] = line_phylum
fw = open("rpS3_to_bin.txt","w")
list_bin = os.listdir("../drep_result/dereplicated_genomes")
for bins in list_bin:
	name = bins.split(".")[0] + "_" + bins.split(".")[1]
	name_sample = bins.split(".")[0]
	path = "../drep_result/dereplicated_genomes/" + bins
	fas = SeqIO.parse(path,"fasta")
	for fa in fas:
		contig_id = name_sample + "__" + fa.id
		if contig_id in dict_map.keys():
			rps3_id = dict_map[contig_id]
			rps3_phylum = dict_phylum_a[rps3_id]
			bin_phylum = dict_bin_phylum[name]
			centroid = dict_rps3_to_centroid[rps3_id]
			fw.write(name + "\t" + bin_phylum + "\t" + rps3_id + "\t" + centroid + "\t" + rps3_phylum + "\n")
