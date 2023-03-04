library(ggplot2)
library(reshape2)

data <- read.table("all_rps3_abundance_persample.txt", header = T, check.names = F, row.names = 1)
df <- melt(data)
df$phylum <- factor(df$phylum,
                    levels = c("Acidobacteria","Actinobacteria","Alphaproteobacteria","Bacteroidetes",
                               "Betaproteobacteria","Chloroflexi","Dadabacteria","Deltaproteobacteria",
                               "Gammaproteobacteria","Gemmatimonadetes","Ignavibacteria","Nitrospinae",
                               "Nitrospirae","Omnitrophica","other","Planctomycetes","Poribacteria",
                               "Thaumarchaeota","unclassify","Zixibacteria"))
mycol <- c("#4e79a7","#d37295","#d4a6c8","#8cd17d","#d4a6c8","#e15759","#a0cbe8","#9d7660",
           "#d4a6c8","#b6992d","#8cd17d","#f28e2b","#86bcb6","#9faaa2","#ffbe7d","#f1ce63",
           "#79706e","#00a98f","#bcbec0","#59a14f")
p <- ggplot(df, aes(x=variable, y=value, fill=phylum)) + geom_bar(stat = "identity",position ="stack") +
  scale_fill_manual(values=mycol) + labs(x = "Sample" , y = "Relative abundance(%)") +
  theme(axis.title=element_text(size=15),axis.text.x = element_text(angle=45, hjust = 1, vjust = 1 ,size = 12),
        axis.text.y = element_text(size = 12),axis.ticks.length=unit(0.15,'cm') ,
      panel.background = element_blank(),axis.line = element_line(color = "black"))
ggsave("phylum-bar.pdf",p,width = 10,height = 12)
