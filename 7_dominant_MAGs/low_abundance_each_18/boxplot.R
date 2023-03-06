library(ggplot2)
rm(list = ls())
setwd("E:/2_sea_metagenomics/6.metabat2/bins_redup_refinem_drep/derep_70_10/4_figure_key_bins/low_abundance_each_visualization")
c_num <- read.table("low_bin_profile_all.txt", header = F, check.names = F)
c_num$V2 <- factor(c_num$V2,levels = c("transport","redox","ncyc","scyc","cazy"))
P1 <- ggplot(c_num,aes(x=V2,y=V1,fill=V2))+
  geom_jitter(fill="#1788bf",width =0.15,height = 0,shape = 21,alpha = 0.8,stroke = 0.1) +
  stat_boxplot(geom = "errorbar",width=0.3,color="black",size = 0.3)+
  geom_boxplot(aes(fill=V2),size=0.05,alpha = 0.8,outlier.shape = 21,outlier.fill="#1788bf",outlier.color="black",outlier.alpha=0.8,outlier.stroke = 0.1)+
  scale_fill_manual(values = c("#89ab26","#c33e50","#139aa9","#e9a047","#5b5f66"))+
  theme_bw()+
  theme(
        axis.text.x=element_text(colour="black",family="Times",size=14,angle = 90, hjust = 1),
        axis.text.y=element_text(family="Times",size=14,face="plain"),
        axis.title.y=element_text(family="Times",size = 14,face="plain"),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "top") +
  ylab("Number of genes") + xlab("")
ggsave("low_bin_profile_all.pdf",P1,width = 4,height = 5)
