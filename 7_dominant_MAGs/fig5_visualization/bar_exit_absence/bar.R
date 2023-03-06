library(ggplot2)
setwd("E:/2_sea_metagenomics/6.metabat2/bins_redup_refinem_drep/derep_70_10/4_figure_key_bins/high_abundance_checked/bar_exit_ absence")
mydata=read.csv("metal.csv",header=F)
ggplot(mydata,aes(x=V1,y=V3,fill=V1))+geom_bar(stat="identity",width = 0.9,position ="stack",color = "black")+
  scale_fill_manual(values=c("#0091CD","#B4A996")) + ylim(0,0.9) +  
  theme(panel.background = element_blank(),axis.line = element_line(color = "black"))
ggsave("metal.pdf", width = 3,height = 3,scale = 1,limitsize = FALSE)
