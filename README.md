# Fe-Mn_nodules_metagenomics
We performed deep metagenomic sequencing of seven sediment-associated communities from surface Fe-Mn sediments from the CCFZ in the East Pacific Ocean. Here we provided all the steps of the analysis of this study, including the code, generated tables and figures, etc.
1_metagenomic_assembly                                                    
fastq_data_link.txt
URL where sequencing data can be downloaded.
megahit.sh
Bash script for metagenomic assembly.
megahit_result
Directory containing the assembled results for each sample. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
quast.sh 
Bash script to evaluate assembly quality.
quast_result
Directory containing the results of the assembly quality for each sample.
all_quast_result.xlsx (Table S2)
Merged file of the results of the assembly quality.
pullseq.sh
Bash script to filter contigs with length less than 1000kb in each assembly.
pullseq_result
Directory containing filtered assemblies. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
prodigal.sh
Bash script for predicting ORFs on filtered contigs.
prodigal_result
Directory containing predicted results for ORFs. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
