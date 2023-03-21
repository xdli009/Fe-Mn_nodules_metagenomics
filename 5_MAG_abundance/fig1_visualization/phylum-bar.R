library(ggplot2)
library(reshape2)

data <- read.csv("merge_phylum.csv", header = T, check.names = F, row.names = 1)

df <- melt(data)
df$phylum <- factor(df$phylum,levels = c("Thermoproteota","Verrucomicrobiota","Planctomycetota","Actinobacteriota","Chloroflexota","Poribacteria","Krumholzibacteriota","Gemmatimonadota","Latescibacterota","KSB1","Bacteroidota","Acidobacteriota","Methylomirabilota","Nitrospirota","Nitrospinota","Tectomicrobia","Desulfobacterota_B","Desulfobacterota_D","Myxococcota","Myxococcota_A","SAR324","Proteobacteria"))
mycol <- c("#00a98f","#bab0ac","#f1ce63","#d37295","#e15759","#79706e","#59a14f","#b6992d","#d7b5a6","#9faaa2","#8cd17d","#4e79a7","#ff9d9a","#86bcb6","#f28e2b","#499894","#fabfd2","#a0cbe8","#9d7660","#b07aa1","#ffbe7d","#d4a6c8")

p <- ggplot(df, aes(x=variable, y=value, fill=phylum)) + geom_bar(stat = "identity",position ="stack") +
  scale_fill_manual(values=mycol) + labs(x = "Sample" , y = "Relative abundance(%)") +
  theme(axis.title=element_text(size=15),axis.text.x = element_text(angle=45, hjust = 1, vjust = 1 ,size = 12),
        axis.text.y = element_text(size = 12),axis.ticks.length=unit(0.15,'cm') ,
      panel.background = element_blank(),axis.line = element_line(color = "black"))
p
ggsave("phylum-bar.pdf",p,width = 8,height = 8)
