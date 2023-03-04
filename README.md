[Github README.md](https://github.com/xdli009/Fe-Mn_nodules_metagenomics/files/10888377/Github.README.md)
# Fe-Mn_nodules_metagenomics
We performed deep metagenomic sequencing of seven sediment-associated communities from surface Fe-Mn sediments from the CCFZ in the East Pacific Ocean. Here we provided all the steps of the analysis of this study, including the code, generated tables and figures, etc.

### 1_metagenomic_assembly                                                    
**fastq_data_link.txt**
URL where sequencing data can be downloaded.
**megahit.sh**
Bash script for metagenomic assembly.
**megahit_result**
Directory containing the assembled results for each sample. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**quast.sh **
Bash script to evaluate assembly quality.
**quast_result**
Directory containing the results of the assembly quality for each sample.
**all_quast_result.xlsx (Table S2)**
Merged file of the results of the assembly quality.
**pullseq.sh**
Bash script to filter contigs with length less than 1000kb in each assembly.
**pullseq_result**
Directory containing filtered assemblies. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**prodigal.sh**
Bash script for predicting ORFs on filtered contigs.
**prodigal_result**
Directory containing predicted results for ORFs. (The files are not uploaded due to their size, but you can run the above bash script to get them.)

### 2_rpS3_gene
**rpS3_Diamond2019.hmm**
The HMM for the alignment of 2249 rpS3 marker sequences.
**hmmer.sh**
Bash script for identifying rpS3 genes.
**ex_rpS3.py**
Python script for extracting rpS3 protein sequences.
**rpS3_fasta     **                              
Directory containing the results of the identification of the rpS3 gene.
**all_rpS3.fasta**
Merged fasta file of all rpS3 protein sequences from 7 samples.
**usearch.sh**
Bash script for clustering all rpS3 protein sequences.
**cluster_dir **
Directory containing the results of rpS3 clustering. (These files are not uploaded because there are too many of them, but you can run the above bash script to get them.)
**rpS3_centroids.fasta**
Representative sequences for each rpS3 protein cluster.
**classification**
**rpS3_centroid_and_ref.fasta**
Merged fasta file containing our 2267 rpS3 representative sequences and the 2249 rpS3 reference sequences.
**tree.sh**
Bash script to build a phylogenetic tree.
**rpS3_centroid_and_ref.trim.phy.treefile**
The tree in newick format.
**rpS3_phylum.txt**
Taxonomic classification of rpS3 SGs at the phylum level.
**abundance**
**get_long_contig.py**
python script to extract the longest contig in each rpS3 protein cluster.
**all_rps3_to_contig_id.txt**
Names of all contigs encoding rpS3 proteins.
**long_contig_info.txt**
Information about the longest contig in each rpS3 protein cluster.
**long_contig.fasta**
Fasta file of all longest contigs.
**index**
Directory containing indexed files for 'long_contig.fasta'.
**mapping**
**bwa.sh**
Bash script for mapping reads to the longest contigs.
**coverm.sh**
Bash script to calculate the coverage of each contig.
**mapping_result**
Directory containing the results of coverage calculating.
**all_abundance.txt**
Merged file of the coverage of each contig in each sample.
**get_rpS3_to_contig.py**
Python script for matching contig's coverage to rpS3's coverage.
**all_rps3_abundance.txt**
The coverage of each rpS3 protein cluster in each sample.
**all_rps3_relative_abundance.xlsx (Table S3)**
The result for calculating the relative abundance of each rpS3 protein cluster based on coverage data using EXCEL.
**visualization**
**species_abundance_bar.R**
R script for visualization of Fig. S2a.
**all_rps3_relative_abundance_average.txt**
Input file for the R script above.
**SGs_abundance_bar.pdf**
PDF file of Fig. S2a.
**phylum-bar.R**
R script for visualization of Fig. S2b.
**all_rps3_abundance_persample.txt**
Input file for the R script above.
**phylum-bar.pdf**
PDF file of Fig. S2b.
**Figure_S2.pdf**
The combined figure generated using Adobe Illustrator.
**Figure_S2.tif**
The TIFF format of Fig. S2.

### 3_genome_binning
**mapping**
**index**
Directory containing indexed files for metagenomic assemblies. (The files are not uploaded due to their size, but you can run the bash script in the directory to get them.)
**bwa.sh**
Bash script to generate sequences map files.
**bwa_result**
Directory containing sequences map files. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**metabat2.sh**
Bash script for metagenome binning.
**coverage_result**
Directory containing the results of coverage profiles. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**bins_result**
Directory containing MAGs for each sample. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**refinem.sh**
Bash script for refining MAGs.
**bins_refinem**
Directory containing the results of refining MAGs. (The files are not uploaded due to their size, but you can run the above bash script to get them.)

### 4_MAG_dereplication
**all_refined_bins**
Directory containing all refined MAGs. (The files are not uploaded due to their size, but you can put all refined MAGs in one directory based on the above results.)
**drep.sh**
Bash script to deduplicate all refined MAGs.
**drep_result**
**dereplicated_genomes**
Directory containing 179 high quality nonredundant MAGs. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**change_newid.sh**
Bash script to change the names of 179 MAGs.
**dereplicated_genomes_newid**
Directory containing 179 MAGs after changing the names. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**change_contig_id.py**
Python script to change the contig names of MAGs.
**dereplicated_genomes_newid_newcontigid**
Directory containing 179 MAGs after changing the contig names.
**gtdbtk.sh**
Bash script for taxonomic classification of 179 MAGs.
**gtdb_result**
Directory containing results of classification.
**MAGs_gtdb_to_rpS3**
**all_rps3_relative_abundance_average_to_info.txt**
Information of rpS3 protein clusters.
**bins_phylum.csv**
Taxonomic classification of MAGs at the phylum level.
**get_rpS3_to_bin.py**
Python script to check the GTDB-based classification with rpS3-based classification.
**rpS3_to_bin.txt**
The result of running the python script above.
**sankey.R**
R script for visualization of Fig. S3.
**rpS3_to_bin_ggplot.txt**
Input file for the R script above.
**Figure_S6.pdf**
PDF file of Fig. S6. (The image is retouched on the output of the R script using Adobe Illustrator.)
**Figure_S6.tif**
The TIFF format of Fig. S6.
**quast.sh**
Bash script to evaluate assembly quality of 179 MAGs.
**MAG_quast**
Directory containing the results of the assembly quality.
**all_drep_bins_info.xlsx (Table S4)**
Information of all nonredundant MAGs.

### 5_MAG_abundance
**index**
Directory containing indexed files for merged 179 MAGs. (The files are not uploaded due to their size, but you can run the bash script in the directory to get them.)
**bwa.sh**
Bash script for mapping reads from each individual metagenome to the 179 MAGs.
**bwa_result**
Directory containing the results of mapping. (The files are not uploaded due to their size, but you can run the above bash script to get them.)
**coverm.sh**
Bash script to calculate the relative abundance of each MAG in each sample.
**abundance**
Directory containing the results of abundance calculating.
**merge.txt (Table S6)**
Merged file of  the relative abundance of each MAG in each sample.
**maping_rate**
**maping_rate.sh**
Bash script to calculate the percentage of the metagenomes that the 179 MAGs represent.
**result**
Directory containing the results of CoverM runs. (The BAM files are not uploaded due to their size, but you can run the above bash script to get them.)
**maping_rate_each_sample.xlsx (Table S5)**
The percentage of the metagenomes that the 179 MAGs represent.
**fig1_visualization**
**phylum-bar.R**
R script for visualization of the relative abundance of these MAGs.
**merge_phylum.csv**
Input file for the R script above.
**phylum-bar.pdf**
The stacked bar chart for showing the relative abundance of these MAGs in seven samples.
**Sequence_data_volume.xlsx**
Sequence size of each sample.
**Sequence_data_volume.pdf**
Visualization for sequence size of each sample using tableau.
**sample_bin_num.xlsx**
Numuber of MAGs for each sample.
**sample_bin_num.pdf**
Visualization for numuber of MAGs for each sample using tableau.
**gtdb_tree.sh**
Bash script to constructe archaeal and bacterial phylogenetic tree.
**gtdbtk.ar122.user_msa.fasta.treefile**
Archaeal tree in newick format.
**gtdbtk.bac120.user_msa.fasta.treefile**
Bacterial tree in newick format.
**gtdb_tree_ar.pdf**
Visualization for archaeal tree using iTOL.
**gtdb_tree_bac.pdf**
Visualization for bacterial tree using iTOL.
**Figure_1.pdf**
PDF file of Fig. 1. (The image is generated by combining the above pictures using Adobe Illustrator.)
**Figure_1.tif**
The TIFF format of Fig. 1.

### 6_MAG_annotataion
**genes_prediction**
**prodigal.sh**
Bash script to predict genes of the 179 MAGs.
**prodigal_result**
Directory containing the results of genes prediction. (These files are compressed.)
**annotation_rRNA**
**barrnap.sh**
Bash script to identify rRNAs of MAGs.
**barrnap_result**
Directory containing the results of rRNA identification.
**get_allbins_rrna.sh**
Bash script to count the number of rRNA per MAG.
**allbins_rrna.csv**
Table of the number of rRNA per MAG.
**annotation_tRNA**
**trnascan.sh**
Bash script to identify tRNAs of MAGs.
**trnascan_result**
Directory containing the results of tRNA identification.
**get_allbins_trna.sh**
Bash script to count the number of tRNA per MAG.
**allbins_trna.csv**
Table of the number of tRNA per MAG.
**annotation_metal_transport_and_redox_reactions**
**bins_phylum.csv**
Taxonomy at the phylum level of each MAG.
**abundance_average.csv**
The mean relative abundance of each MAG.
**FenGenie.sh**
Bash script to identify proteins for iron redox reactions.
**FeGenie-geneSummary_redox.xlsx**
Annotated results after filtering the results of running the above code.
**database_custom
**Custom blastp databases for other metals redox reactions.
**blastp_custom.sh**
Bash script to identify proteins for other metals redox reactions.
**blastp_custom_result**
Directory containing the results of running the bash script above.
**statistic_custom.py**
Python script for collating the above results.
**statistic_custom_result.xlsx**
Statistical result for annotations on redox reactions of other metals. (Since some query proteins matched both metal redox proteins and metal transport proteins, we manually corrected the result of the above python script.)
**databas_TCDB**
The Transporter Classification Database (TCDB).
**blastp_TCDB.sh**
Bash script to annotate membrane metal transport proteins.
**blastp_TCDB_result**
Directory containing the results of running the bash script above.
**statistic_TCDB.py**
Python script for collating the above results.
**statistic_TCDB_result.xlsx**
Statistical result for annotations on metal transport. (Since some query proteins matched both metal redox proteins and metal transport proteins, we manually corrected the result of the above python script.)
**metal_transporter_cluster_id.txt**
Family of metal transporters.
**NR_check**
**all_anno.txt**
IDs of all proteins involved in metal transport and redox reactions.
**get_genes_calls.py**
Python script to get the fasta files of each protein above.
**blastp.slm**
Bash script for re-annotating these proteins using blastp against the NR database. (The NR database can be downloaded from NCBI.)
**all_proteins_annotated**
Directory containing the fasta files of each protein and the corresponding annotated results. (These files are not uploaded because there are too many of them, but you can run the above python and bash script to get them.)
**get_nr_check.py**
Python script for collating the annotated results of NR database.
**all_anno_to_nr.txt**
The result of the above python script.
**all_anno_to_nr_reason.xlsx (Table S13)**
Checked annotations involved in metal transport and redox reactions.
**check_passed_id.txt**
Correctly annotated gene IDs.
**bin_metal_tcdb_phylum_abundance.txt**
Information of MAGs containing genes before annotation checking.
**get_passed_gene_info.py**
Python script to get information of MAGs containing correctly annotated genes.
**bin_metal_tcdb_phylum_abundance_passed.txt**
Information of MAGs containing correctly annotated genes.
**bin_metal_transport_phylum_abundance_passed.xlsx (Table S7)**
Information of metal redox annotation in the 179 MAGs.
**bin_metal_redox_phylum_abundance_passed.xlsx (Table S8)**
Information of TCDB's annotation in the 179 MAGs.
**iron_oxidation_reduction.xlsx (Table S9)**
The list of proteins involved in iron oxidation and iron reduction.
**fig2_figS4_visualization**
**bin_metal_tcdb_phylum_abundance_passed_uniq.xlsx**
Converts to a annotated list of whether the MAGs has the functions.
**bin_metal_tcdb_phylum_abundance_passed_uniq.twb**
Visualization for composition of MAGs which contain the genes encoding the related proteins using tableau.
**bin_metal_tcdb_phylum_abundance_passed_uniq.pdf**
PDF file output by Tableau.
**Figure_2.pdf**
PDF file of Fig. 2. (These images were generated by combining the pictures output by tableau using Adobe Illustrator.)
**Figure_2.tif**
The TIFF format of Fig. 2.
**Figure_S4.pdf**
PDF file of Fig. S4. (These images were generated by combining the pictures output by tableau using Adobe Illustrator.)
**Figure_S4.tif**
The TIFF format of Fig. S4.
**annotation_CAZymes**
**hmmscan.sh**
Bash script to identify carbohydrate degradation enzymes (CAZymes). (The 'dbCAN-HMMdb-V8.txt' can be downloaded from https://bcb.unl.edu/dbCAN2/download/.)
**dom_tbl**
Directory containing the results of running the bash script above.
**statistic_bins.py**
Python script for collating the above results.
**statistic_bins_CAZy.csv**
Statistical result for annotations of CAZymes.
**statistic_bins_CAZy_MAGs_info.csv (Table S10)**
Based on the above statistical result, the classification and abundance of each MAG were added.
**matrix_to_list.py**
Python script to convert the above result in matrix form to the result in list form.
**statistic_bins_CAZy_MAGs_info_list.txt**
Statistical result for annotations of carbohydrate degradation enzymes in list form.
**phylum.txt**
Taxonomic classification of MAGs at the phylum level.
**statistic_phylum_CAZy.py**
Python script to summarize percentage of genomes within each phylum which contained CAZymes.
**statistic_phylum_CAZy.csv (Table S11)**
The result of running the python script above.
**fig3_visualization**
**melt.R**
R script to convert the file 'statistic_phylum_CAZy.csv'** **to the result in list form.
**cazy_tableau.csv**
The result of running the R script above. (This file is used for tableau's input file.)
**Figure_3a.twb**
Visualization for the above result using Tableau.
**Figure_3a.pdf**
PDF file output by Tableau.
**bins_cazy_num.csv**
Number of CAZymes per MAG.
**boxplot.R**
R script for visualization of Fig. 3b.
**Figure_3b.pdf**
PDF file of Fig. 3b.
**Figure_3.pdf**
PDF file of Fig. 3. (The image is generated by combining the above pictures using Adobe Illustrator.)
**Figure_3.tif**
The TIFF format of Fig. 3.
**annotation_nitrogen_and_sulfur_metabolism**
**database**
NCycDB and SCycDB.
**blastp.sh**
Bash script to annotate proteins for nitrogen and sulfur cycling.
**blastp_result**
Directory containing the results of running the bash script above.
**eggnog.sh**
Bash script for re-annotating these proteins using eggNOG-mapper v2.1.2.
**eggnog_result**
Directory containing the results of running the bash script above.
**all.annotations**
Merged above results.
**statistic.py**
Python script for collating the results annotated using NCycDB, SCycDB and eggNOG-mapper.
**NCyc_eggnog_result.txt  &  SCyc_eggnog_result.txt**
The result of the above python script.
**ncyc_scyc_eggnog_check.xlsx (Table S14)**
Checked annotations involved in nitrogen and sulfur metabolism.
**ncyc_scyc_eggnog_passed.txt**
Correctly annotations.
**fig4_visualization**
**get_table_and_fig_input.py**
Python script to change format of annotations file. We only count whether the MAGs contain the functional proteins, regardless of the copy number. We consider that the genome of MAG is incomplete due to the limitation of metagenomic technology. Thus for an operon, if a MAG is predicted to have one of these proteins, then the MAG is considered to contain that function. It is worth noting that in many cases MAGs contain complete operons.
**ncyc_scyc_bin_table_all.txt (Table S12)  &  ncyc_scyc_gene_table_all.txt**
The result of the above python script.
**melt.R**
R script to convert the file 'ncyc_scyc_bin_table_all.txt'** **to the result in list form.
**ncyc_scyc_bin_table_melt_all.csv**
The result of running the R script above.
**get_order.py**
Python script to summarize number of genomes within each phylum which contained nitrogen and sulfur metabolic proteins.
**ncyc_scyc_bin_table_melt_order_all.csv**
The result of running the python script above.
**ncyc_scyc_bin_table_melt_order_excel_all.csv**
Sorted result in excel.
**phylum_color.txt**
The color corresponding to each phylum in the visualization.
**get_R.py**
Python script to get R scripts that visualize the number of MAGs containing each gene.
**R**
Directory containing all R scripts, input and output results.
**Figure_4.pdf**
PDF file of Fig. 4. (The images were generated by combining pictures from the above directory using Adobe Illustrator.)
**Figure_4.tif**
The TIFF format of Fig. 4.
**MnxG_MoxA_CDsearch**
**moxA_mnxG_proteins.fasta**
Sequence of MnxG and MoxA proteins.
**hitdata_superfamily.txt**
The result of conserved domains of MnxG and MoxA proteins detected using NCBI's CD-search tool.
**MoxA_MnxG_CDD.xml**
Visualization for conserved domains using IBS.
**Figure_S3.pdf**
PDF file output by IBS and retouched using Adobe Illustrator.
**Figure_S3.tif**
The TIFF format of Fig. S3.

### 7_key_MAGs
**high_abundance_bin_id.txt**
IDs of 18 high relative abundance MAGs.
**get_gene_profile_metal_tcdb.py**
Python script to get metal transport and redox profile of these 18 MAGs.
**high_bin_metal_tcdb_phylum_abundance_passed.txt**
The result of running the python script above.
**get_gene_profile_ncyc_scyc.py**
Python script to get nitrogen and sulfur metabolic profile of these 18 MAGs.
**high_bin_nitrogen_sulfur_phylum_abundance_passed.txt**
The result of running the python script above.
**get_gene_profile_cazy.py**
Python script to get carbohydrate degradation profile of these 18 MAGs.
**high_bin_cazy_phylum_abundance_passed.txt**
The result of running the python script above.
**fig5_visualization**
**bin_average_abundance_phylum.txt**
The mean relative abundance and taxonomy of each MAG.
**species_abundance_bar.R**
R script for visualization of Fig. 5a.
**Figure_5a.pdf**
PDF file of Fig. 5a.
**high_abundance_bins_info.csv**
Information of 18 high relative abundance MAGs.
**high_abundance_all_network_checked.txt**
All functional profile of these 18 MAGs (manually checked).
**high_abundance_all_network.cys**
Visualization for overview of the metabolic functions of these MAGs using cytoscape.
**high_abundance_all_network.pdf**
PDF file output by cytoscape.
**bar_exit_ absence**
Directory containing the histograms that show the total number of detected and undetected genes for each functional category in 18 MAGs.
**Figure_5.pdf**
PDF file of Fig. 5. (The images were generated by combining above pictures using Adobe Illustrator.)
**Figure_5.tif**
The TIFF format of Fig. 5.
**low_abundance_each_18**
**low_abundance_bin_id.txt**
IDs of the remaining MAGs other than the dominant MAGs.
**metal_transport_proteins.txt**
Organized annotations involved in metal transport.
**metal_redox_proteins.txt**
Organized annotations involved in metal redox.
**ncyc_proteins.txt**
Organized annotations involved in nitrogen metabolism.
**scyc_proteins.txt**
Organized annotations involved in sulfur metabolism.
**CAZy_proteins.txt**
Organized annotations involved in carbohydrate degradation.
**get_gene_profile_all.py**
Python script to randomly selected 18 MAGs in 100 replicates among the remaining MAGs and calculated the number of genes for each functional category.
**low_bin_profile_all.txt**
The result of running the python script above.
**boxplot.R**
R script for visualization of the number of genes for each functional category among the remianing MAGs.
**low_bin_profile_all.pdf**
The result of running the R script above.
**num_gene_comparsion.xlsx**
The table comparing the number of genes in each functional profile of dominant MAGs and remaining MAGs.
**Figure_S5.pdf**
PDF file of Fig. S5. (The images were generated by combining above picture and table using Adobe Illustrator.)
**Figure_S5.tif**
The TIFF format of Fig. S5.

### 8_conclusion
**bin_phylum_abundance_all_cycle_merge.txt**
All microbial-dominated ecological functions.
**get_all_key.py**
Python script to calculate the width of lines representing the total relative abundance of key and other MAGs performing each function.
 **get_all_key.txt**
The result of running the python script above.
**Figure_6.pdf**
PDF file of Fig. 6. (The elements of the image were drawn using Adobe Illustrator based on the above data.)
**Figure_6.tif**
The TIFF format of Fig. 6.
