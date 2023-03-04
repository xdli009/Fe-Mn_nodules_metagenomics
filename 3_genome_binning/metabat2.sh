for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
jgi_summarize_bam_contig_depths --outputDepth ./metabat2_result/${name}_depth.txt ./mapping/bwa_result/${name}.redup.bam
#Minimum size of a contig for binning is the default value of 2500
metabat2 -t 9 -i ../1_metagenomics_assembly/pullseq_result/${name}_1000bp.fasta -a ./metabat2_result/${name}_depth.txt -o ./bins/${name}
done
