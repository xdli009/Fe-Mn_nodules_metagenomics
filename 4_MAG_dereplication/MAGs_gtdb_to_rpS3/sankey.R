library(ggalluvial)
library(reshape2)
mydata<-read.table("rpS3_to_bin_ggplot.txt",header = T,check.names = F)
df_lodes <- to_lodes_form(mydata,key ="x", value = "stratum", id = "alluvium",axes =1:2)
df_lodes$stratum <- factor(df_lodes$stratum,
                    levels = c("Acidobacteriota","Actinobacteriota","Proteobacteria","Bacteroidota",
                               "Chloroflexota","Desulfobacterota_B","Desulfobacterota_D","Gemmatimonadota",
                               "Krumholzibacteriota","KSB1","Latescibacterota","Methylomirabilota",
                               "Myxococcota","Myxococcota_A","Nitrospinota","Nitrospirota","Planctomycetota",
                               "SAR324","Tectomicrobia","Thermoproteota","Verrucomicrobiota","Poribacteria","Acidobacteria",
                               "Actinobacteria","Alphaproteobacteria","Bacteroidetes","Betaproteobacteria",
                               "Chloroflexi","Dadabacteria","Deltaproteobacteria","Gammaproteobacteria",
                               "Gemmatimonadetes","Ignavibacteria","Nitrospirae","Planctomycetes",
                               "Thaumarchaeota","unclassified","Verrucomicrobia"))
mycol <- c("#4e79a7","#d37295","#d4a6c8","#8cd17d","#e15759","#fabfd2","#a0cbe8","#b6992d","#59a14f",
           "#9faaa2","#d7b5a6","#ff9d9a","#9d7660","#b07aa1","#f28e2b","#86bcb6","#f1ce63","#ffbe7d",
           "#499894","#00a98f","#bab0ac","#79706e","#4e79a7","#d37295","#d4a6c8","#8cd17d","#d4a6c8",
           "#e15759","#a0cbe8","#9d7660","#d4a6c8","#b6992d","#8cd17d","#86bcb6","#f1ce63","#00a98f",
           "#bcbec0","#bab0ac")
p<-ggplot(df_lodes,aes(x = x, stratum =stratum, alluvium = alluvium,
                        fill = stratum, label = stratum)) +
  scale_x_discrete(expand = c(0, 0)) +
  geom_flow(width = 0.15, knot.pos = 0.1) +
  geom_stratum(color="grey20",width = 1/7) +
  geom_text(stat = "stratum", size = 2,color="black")  +
  xlab("") + ylab("") + scale_fill_manual(values = mycol) +
  theme_bw() +
  theme(panel.grid =element_blank()) +
  theme(panel.border = element_blank()) +
  theme(axis.line = element_blank(),axis.ticks =element_blank(),axis.text.y =element_blank())
ggsave(p, file='Supplementary_Figure_3.pdf', width=6, height=12)
