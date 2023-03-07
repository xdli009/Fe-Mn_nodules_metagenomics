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
	mkdir = "mkdir " + bins
	os.system(mkdir)
	call_path = bins + "/" + bins + "_proteins_annotation.txt"
	call_fw = open(call_path,"w")
	call_fw.write("Gene ID" + "\t" + "Contig ID" + "\t" + "Start" + "\t" + "End" + "\t" + "Strand" + "\t" + "Function" + "\t" + "Amino acid sequence" + "\n")
	faa_path = "../genes_prediction/prodigal_result/" + bins + "_proteins.faa" 
	faa_dict = SeqIO.to_dict(SeqIO.parse(faa_path,"fasta"))
	for genes in dict1[bins].keys():
		contig = genes.rsplit("_",1)[0]
		start = faa_dict[genes].description.split(" # ")[1]
		end = faa_dict[genes].description.split(" # ")[2]
		if faa_dict[genes].description.split(" # ")[3] == "-1":
			strand = "-"
		elif faa_dict[genes].description.split(" # ")[3] == "1":
			strand = "+"
		annotation = dict1[bins][genes]
		amino = str(faa_dict[genes].seq)
		call_fw.write(genes + "\t" + contig + "\t" + start + "\t" + end + "\t" + strand + "\t" + annotation + "\t" + amino + "\n")
	cp_genome = "cp ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/" + bins + ".fa ./" + bins + "/" + bins + "_genome.fna"
	os.system(cp_genome)
	cp_faa = "cp ../genes_prediction/prodigal_result/" + bins + "_proteins.faa ./" + bins + "/" + bins + "_proteins.faa"
	os.system(cp_faa)
