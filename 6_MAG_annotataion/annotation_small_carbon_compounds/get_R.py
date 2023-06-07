fr_color = open("phylum_color.txt","r").read().splitlines()
dict_color = {}
for line in fr_color:
    phylum = line.split()[1]
    color = line.split()[0]
    dict_color[phylum] = color
fr_ns = open("simple_compounds_ko_id_phylum_redup_order_excel.csv","r").read().splitlines()
dict_ns = {}
dict_list = {}
for line in fr_ns:
    gene = line.split(",")[0]
    phylum = line.split(",")[1]
    num = line.split(",")[2]
    dict_list.setdefault(gene,[]).append(phylum)
    dict_ns.setdefault(gene,{})[phylum] = num
for gene in dict_list.keys():
    path_csv = "./R/" + gene + ".csv" 
    fw_csv = open(path_csv,"w")
    fw_csv.write("gene,phylum,num" + "\n")
    path_r = "./R/" + gene + ".R"
    fw_r = open(path_r,"w")
    fw_r.write("library(ggplot2)" + "\n" + 'data <- read.csv("' + gene + '.csv", header = T, check.names = F)' + "\n")
    level_phylum = ""
    level_color = ""
    for phylum in dict_list[gene]:
        fw_csv.write(gene + "," + phylum + "," + dict_ns[gene][phylum] + "\n")
        level_phylum = level_phylum + '"' + phylum + '",'
        level_color = level_color + '"' + dict_color[phylum] + '",'
    level_phylum = level_phylum[0:-1]
    level_color = level_color[0:-1]
    fw_r.write('data$phylum <- factor(data$phylum,levels = c(' + level_phylum + '))' + "\n")
    fw_r.write('mycol <- c(' + level_color + ')' + "\n")
    fw_r.write('p <- ggplot(data, aes(x=gene, y=num, fill=phylum)) + geom_bar(stat = "identity",position ="fill") + scale_fill_manual(values=mycol) + labs(x = "Sample" , y = "Relative abundance(%)") + theme(axis.title=element_text(size=15),axis.text.x = element_text(angle=45, hjust = 1, vjust = 1 ,size = 12),axis.text.y = element_text(size = 12),axis.ticks.length=unit(0.15,"cm") ,panel.background = element_blank(),axis.line = element_line(color = "black"))' + "\n")
    fw_r.write('ggsave("' + gene + '.pdf",p,width = 8,height = 8)')
