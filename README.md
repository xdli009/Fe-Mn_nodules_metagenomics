# Fe-Mn_nodules_metagenomics
We performed deep metagenomic sequencing of seven sediment-associated communities from surface Fe-Mn sediments from the CCFZ in the East Pacific Ocean. Here we provided all the steps of the analysis of this study, including the code, generated tables and figures, etc.

## 1_metagenomic_assembly
  * #### fastq_data_link.txt    
    URL where sequencing data can be downloaded.  
  * #### megahit.sh  
    Bash script for metagenomic assembly.  
  * #### megahit_result  
    Directory containing the assembled results for each sample. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
  * #### quast.sh 
    Bash script to evaluate assembly quality.
  * #### quast_result
    Directory containing the results of the assembly quality for each sample.
  * #### all_quast_result.xlsx (Table S2)
    Merged file of the results of the assembly quality.
  * #### pullseq.sh
    Bash script to filter contigs with length less than 1000kb in each assembly.
  * #### pullseq_result
    Directory containing filtered assemblies. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
  * #### prodigal.sh
    Bash script for predicting ORFs on filtered contigs.
  * #### prodigal_result
    Directory containing predicted results for ORFs. (The files are not uploaded due to their size, but you can run the above bash script to get them.)

# 2_rpS3_gene
rpS3_Diamond2019.hmm
The HMM for the alignment of 2249 rpS3 marker sequences.
hmmer.sh
Bash script for identifying rpS3 genes.
ex_rpS3.py
Python script for extracting rpS3 protein sequences.
rpS3_fasta                                   
Directory containing the results of the identification of the rpS3 gene.
all_rpS3.fasta
Merged fasta file of all rpS3 protein sequences from 7 samples.
usearch.sh
Bash script for clustering all rpS3 protein sequences.
cluster_dir 
Directory containing the results of rpS3 clustering. (These files are not uploaded because there are too many of them, but you can run the above bash script to get them.)
rpS3_centroids.fasta
Representative sequences for each rpS3 protein cluster.
classification
rpS3_centroid_and_ref.fasta
Merged fasta file containing our 2267 rpS3 representative sequences and the 2249 rpS3 reference sequences.
tree.sh
Bash script to build a phylogenetic tree.
rpS3_centroid_and_ref.trim.phy.treefile
The tree in newick format.
rpS3_phylum.txt
Taxonomic classification of rpS3 SGs at the phylum level.
abundance
get_long_contig.py
python script to extract the longest contig in each rpS3 protein cluster.
all_rps3_to_contig_id.txt
Names of all contigs encoding rpS3 proteins.
long_contig_info.txt
Information about the longest contig in each rpS3 protein cluster.
long_contig.fasta
Fasta file of all longest contigs.
index
Directory containing indexed files for 'long_contig.fasta'.
mapping
bwa.sh
Bash script for mapping reads to the longest contigs.
coverm.sh
Bash script to calculate the coverage of each contig.
mapping_result
Directory containing the results of coverage calculating.
all_abundance.txt
Merged file of the coverage of each contig in each sample.
get_rpS3_to_contig.py
Python script for matching contig's coverage to rpS3's coverage.
all_rps3_abundance.txt
The coverage of each rpS3 protein cluster in each sample.
all_rps3_relative_abundance.xlsx (Table S3)
The result for calculating the relative abundance of each rpS3 protein cluster based on coverage data using EXCEL.
visualization
species_abundance_bar.R
R script for visualization of Fig. S2a.
all_rps3_relative_abundance_average.txt
Input file for the R script above.
SGs_abundance_bar.pdf
PDF file of Fig. S2a.
phylum-bar.R
R script for visualization of Fig. S2b.
all_rps3_abundance_persample.txt
Input file for the R script above.
phylum-bar.pdf
PDF file of Fig. S2b.
Figure_S2.pdf
The combined figure generated using Adobe Illustrator.
Figure_S2.tif
The TIFF format of Fig. S2.
