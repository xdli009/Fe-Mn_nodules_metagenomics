for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
refinem scaffold_stats -c 16 --genome_ext fa ../1_metagenomics_assembly/pullseq_result/${name}_1000bp.fasta ./bins_result/${name} ./bins_refinem/${name}_output_dir ./mapping/bwa_result/${name}.redup.bam
refinem outliers ./bins_refinem/${name}_output_dir/scaffold_stats.tsv ./bins_refinem/${name}_output_dir/${name}_outlier
refinem filter_bins --genome_ext fa ./bins_result/${name} ./bins_refinem/${name}_output_dir/${name}_outlier/outliers.tsv ./bins_refinem/${name}_output_dir/filtered_output_bins
refinem call_genes -c 12 --genome_ext fa ./bins_refinem/${name}_output_dir/filtered_output_bins ./bins_refinem/${name}_output_dir/gene_output
refinem taxon_profile -c 12 --tmpdir ./temp ./bins_refinem/${name}_output_dir/gene_output ./bins_refinem/${name}_output_dir/scaffold_stats.tsv gtdb_r95_protein_db.2020-07-30.faa.gz gtdb_r95_taxonomy.2020-07-30.tsv ./bins_refinem/${name}_output_dir/taxon_profile_output
refinem taxon_filter -c 12 ./bins_refinem/${name}_output_dir/taxon_profile_output ./bins_refinem/${name}_output_dir/taxon_filter.tsv
refinem filter_bins --genome_ext fa ./bins_refinem/${name}_output_dir/filtered_output_bins ./bins_refinem/${name}_output_dir/taxon_filter.tsv ./bins_refinem/${name}_output_dir/taxon_filtered_output_bins
done
