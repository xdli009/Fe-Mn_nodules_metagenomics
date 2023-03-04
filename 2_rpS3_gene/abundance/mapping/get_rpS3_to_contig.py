fr1=open("all_abundance.txt","r").read().splitlines()
dict1 = {}
for line in fr1:
	id1 = line.split()[0]
	dict1[id1]=line
fr2=open("../long_contig_info.txt","r").read().splitlines()
fw = open("all_rps3_abundance.txt","w")
for line in fr2:
	id1 = line.split()[3]
	info = dict1[id1]
	fw.write(line + "\t" + info + "\n")	
