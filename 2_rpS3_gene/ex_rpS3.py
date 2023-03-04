from Bio import SeqIO
import os
list_r = os.listdir("./rpS3_fasta")
for r in list_r:
	if ".tbl" in r:
		list_fw = []
		name = r.split("_rpS3")[0]
		path_r = "./rpS3_fasta/" + r
		path_fasta = "../1_metagenomics_assembly/prodigal_result/" + name + ".faa"
		seqs = SeqIO.parse(path_fasta, "fasta")
		list_id = []
		fr_r = open(path_r,"r").read().splitlines()
		for i in fr_r:
			if not i.startswith("#"):
				i_id = i.split()[0]
				list_id.append(i_id)
		for fa in seqs:
			fa_id = fa.id
			if fa_id in list_id:
				list_fw.append(fa)
		path_fw = "./rpS3_fasta/" + name + "_rpS3.fasta" 
		SeqIO.write(list_fw,path_fw,"fasta")
