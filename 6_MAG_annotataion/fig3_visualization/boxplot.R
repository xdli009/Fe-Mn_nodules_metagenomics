library(ggplot2)
library(RColorBrewer)
c_num <- read.csv("bins_cazy_num.csv", header = T, check.names = F, row.names = 1)
P1 <- ggplot(c_num,aes(x=phylum,y=cazy_num,fill=phylum))+
  geom_jitter(aes(size=Abundance),fill="#BDBDBD",width =0.15,height = 0,shape = 21,alpha = 0.8,stroke = 0.1) +
  stat_boxplot(geom = "errorbar",width=0.3,color="black",size = 0.3)+
  geom_boxplot(aes(fill=phylum),size=0.1,alpha = 0.8,outlier.shape = 21,outlier.fill="#BDBDBD",outlier.color="black",outlier.alpha=0.8,outlier.stroke = 0.1)+
  scale_fill_manual(values = c("#4e79a7","#d37295","#8cd17d","#e15759","#fabfd2","#a0cbe8","#b6992d","#59a14f","#9faaa2","#d7b5a6","#ff9d9a","#9d7660","#b07aa1","#f28e2b","#86bcb6","#f1ce63","#79706e","#d4a6c8","#ffbe7d","#499894","#00a98f","#bab0ac"))+
  ggtitle("CAZy enzyme counts and diversity")+
  theme_bw()+
  theme(
        axis.text.x=element_text(colour="black",family="Times",size=14,angle = 90, hjust = 1),
        axis.text.y=element_text(family="Times",size=14,face="plain"),
        axis.title.y=element_text(family="Times",size = 14,face="plain"),
        plot.title = element_text(family="Times",size=15,face="bold",hjust = 0.5),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "top") +
  ylab("Total counts per MAG") + xlab("")
ggsave("Figure_3b.pdf",p,width = 25,height = 20)
  
