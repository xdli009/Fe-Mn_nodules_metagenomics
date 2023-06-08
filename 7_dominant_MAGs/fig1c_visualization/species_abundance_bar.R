data <- read.table("bin_average_abundance_phylum.txt",check.names = FALSE,header = T)
data$Genome = factor(data$Genome,
                     levels=c("KW1-S08_123","KW1-S08_155","A5-S03_29","KW1-S05_45","A5-S03_68","KW1-S11_18",
                              "KW1-S11_146","KW1-S15_293","A5-S03_30","KW1-S05_82","KW1-S08_122","KW1-S15_262",
                              "A5-S03_71","A5-S03_47","KW1-S08_128","A5-S03_104","A5-S04_200","A5-S04_119",
                              "KW1-S08_268","KW1-S05_127","A5-S04_125","KW1-S15_188","KW1-S15_126","A5-S04_30",
                              "KW1-S21_6","KW1-S05_81","KW1-S15_144","KW1-S21_141","A5-S04_114","KW1-S21_193",
                              "KW1-S08_186","A5-S03_163","KW1-S21_138","KW1-S11_81","A5-S03_100","KW1-S08_121",
                              "KW1-S05_12","KW1-S15_8","KW1-S11_176","A5-S04_155","KW1-S21_238","KW1-S21_28",
                              "KW1-S15_16","KW1-S21_196","KW1-S21_85","KW1-S15_197","KW1-S08_12","A5-S03_93",
                              "KW1-S08_227","KW1-S15_266","KW1-S05_148","KW1-S11_180","A5-S03_4","KW1-S11_109",
                              "A5-S04_22","KW1-S08_226","KW1-S21_271","KW1-S21_115","KW1-S08_198","KW1-S08_133",
                              "KW1-S21_197","KW1-S21_32","KW1-S05_85","A5-S03_6","KW1-S11_120","KW1-S11_87",
                              "KW1-S11_42","KW1-S11_179","KW1-S15_187","A5-S04_79","KW1-S08_30","A5-S04_33",
                              "A5-S03_147","KW1-S11_190","A5-S04_187","KW1-S05_126","KW1-S05_112","KW1-S15_72",
                              "KW1-S15_98","KW1-S11_163","KW1-S11_24","A5-S04_136","KW1-S21_174","A5-S03_156",
                              "KW1-S05_124","KW1-S08_200","A5-S04_75","KW1-S15_162","KW1-S15_31","KW1-S11_125",
                              "KW1-S05_108","A5-S04_226","KW1-S15_306","KW1-S08_192","KW1-S05_59","KW1-S15_75",
                              "A5-S04_131","A5-S03_18","KW1-S15_2","KW1-S15_279","KW1-S08_89","A5-S03_121",
                              "KW1-S08_134","KW1-S15_218","A5-S04_95","KW1-S21_82","A5-S04_220","KW1-S21_260",
                              "KW1-S08_280","KW1-S08_213","KW1-S05_43","KW1-S11_103","A5-S04_85","KW1-S21_242",
                              "KW1-S05_58","KW1-S11_156","KW1-S15_234","KW1-S21_231","KW1-S15_135",
                              "KW1-S11_157","KW1-S08_236","KW1-S08_251","KW1-S08_62","KW1-S15_137",
                              "KW1-S08_208","KW1-S05_110","KW1-S15_41","A5-S03_33","KW1-S15_96","KW1-S15_14",
                              "KW1-S15_227","KW1-S21_104","KW1-S08_237","KW1-S05_77","A5-S04_18","KW1-S15_200",
                              "KW1-S21_168","A5-S04_105","KW1-S15_112","KW1-S11_124","KW1-S15_23",
                              "KW1-S15_115","A5-S04_112","KW1-S21_123","KW1-S15_267","KW1-S08_28",
                              "KW1-S11_145","KW1-S05_53","KW1-S11_65","KW1-S15_149","KW1-S08_17",
                              "KW1-S21_52","KW1-S15_211","KW1-S15_114","KW1-S08_242","KW1-S21_189",
                              "KW1-S08_222","KW1-S08_24","A5-S04_70","KW1-S21_27","KW1-S11_99","KW1-S08_144",
                              "KW1-S15_132","KW1-S08_46","KW1-S15_215","KW1-S21_73","KW1-S08_233",
                              "KW1-S15_183","KW1-S11_89","KW1-S08_174","KW1-S21_160","KW1-S15_117",
                              "KW1-S05_141","KW1-S11_15","KW1-S21_144","A5-S03_23","A5-S04_77","KW1-S08_229",
                              "KW1-S15_97"))
data$phylum <- factor(data$phylum,levels = c("Thermoproteota","Verrucomicrobiota","Planctomycetota",
                                             "Actinobacteriota","Chloroflexota","Poribacteria",
                                             "Krumholzibacteriota","Gemmatimonadota","Latescibacterota",
                                             "KSB1","Bacteroidota","Acidobacteriota","Methylomirabilota",
                                             "Nitrospirota","Nitrospinota","Tectomicrobia",
                                             "Desulfobacterota_B","Desulfobacterota_D","Myxococcota",
                                             "Myxococcota_A","SAR324","Proteobacteria"))
mycol <- c("#00a98f","#bab0ac","#f1ce63","#d37295","#e15759","#79706e","#59a14f","#b6992d","#d7b5a6",
           "#9faaa2","#8cd17d","#4e79a7","#ff9d9a","#86bcb6","#f28e2b","#499894","#fabfd2","#a0cbe8",
           "#9d7660","#b07aa1","#ffbe7d","#d4a6c8")
p <- ggplot(data=data, aes(x=Genome, y=average, fill=phylum))+
     geom_bar(stat = "identity",colour="black",size=0.05)  +  
     scale_fill_manual(values = mycol) + 
     theme(panel.grid.major = element_line(color = 'transparent'), 
           panel.background = element_rect(color = 'black', fill = 'transparent'))
ggsave("Figure_1c.pdf",p,width = 25,height = 13)


