fr1 = open("statistic_bins_CAZy_MAGs_info.csv","r").read().splitlines()
fw = open("statistic_bins_CAZy_MAGs_info_list.txt","w")
list_gene = fr1[0].split(",")
for line in fr1[1:]:
    bins = line.split(",")[0]
    phylum = line.split(",")[2]
    abundance = line.split(",")[8]
    i = 9
    for gene in line.split(",")[9:]:
        if gene == "1":
            gene_type = list_gene[i]
            fw.write(bins + "\t" + phylum + "\t" + abundance + "\t" + gene_type + "\n")
        i = i + 1
