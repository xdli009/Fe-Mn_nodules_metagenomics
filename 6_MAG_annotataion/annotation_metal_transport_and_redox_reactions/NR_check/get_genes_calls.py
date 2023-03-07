import os 
from Bio import SeqIO

dict1 = {}
fr1 = open("all_anno.txt","r").read().splitlines()
for line in fr1[1:]:
	genes = line.split()[0]
	bins = genes.split("_cg")[0]
	name = line.split()[1]
	dict1.setdefault(bins,{})[genes] = name

for bins in dict1.keys():
	faa_path = "../../genes_prediction/prodigal_result/" + bins + "_proteins.faa" 
	faa_dict = SeqIO.to_dict(SeqIO.parse(faa_path,"fasta"))
	for genes in dict1[bins].keys():
		call_path = "all_proteins_annotated/" + genes + ".faa"
		amino = faa_dict[genes]
		SeqIO.write(amino,call_path,"fasta")
