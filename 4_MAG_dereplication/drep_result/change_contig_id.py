import os
from Bio import SeqIO

list1=os.listdir("./dereplicated_genomes_newid/")
for file1 in list1:
	path1="./dereplicated_genomes_newid/" + file1
	name=file1.split(".fa")[0]
	path2= "./dereplicated_genomes_newid_newcontigid/" + name + ".fa"
	num=int(1)
	records=[i for i in SeqIO.parse(path1,"fasta")]
	for record in records:
		nameid = name + "_cg" + str(num)
		record.id = nameid
		num = num +1
	SeqIO.write(records,path2,"fasta")
