library(ggplot2)

data <- read.table("all_rps3_relative_abundance_average.txt",check.names = FALSE,header = T)
data$phylum_merge = factor(data$phylum_merge,
                     levels=c('Firmicutes','Elusimicrobia','Omnitrophica',
                              'Parcubacteria','Lentisphaerae','Verrucomicrobia',
                              'Armatimonadetes','DPANN_Woesearchaeota','Zixibacteria','Deltaproteobacteria',
                              'Nitrospinae','other','Poribacteria','Dadabacteria',
                              'Betaproteobacteria','Ignavibacteria','Actinobacteria',
                              'Bacteroidetes','Nitrospirae','Gemmatimonadetes',
                              'Chloroflexi','Acidobacteria','Planctomycetes','unclassify','Thaumarchaeota',
                              'Gammaproteobacteria','Alphaproteobacteria'))
data$type = factor(data$type,levels = c('low','high'))
p <- ggplot(data=data, aes(x=phylum_merge, y=average, fill=type))+
     geom_bar(stat = "identity",position="stack",colour="black",size = 0.01) + coord_flip() +  
     scale_fill_manual(values = c("#bcbec0", "#cd2626")) + 
     theme(panel.grid.major = element_line(color = 'transparent'), panel.background = element_rect(color = 'black', fill = 'transparent'), 
     plot.title = element_text(hjust = 0.5)) 
ggsave(p, file='SGs_abundance_bar.pdf', width=6, height=6)  
