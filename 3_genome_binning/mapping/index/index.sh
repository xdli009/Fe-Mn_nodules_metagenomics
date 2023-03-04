for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
bwa index -a bwtsw ../../../1_metagenomics_assembly/pullseq_result/${name}_1000bp.fasta -p ./${name}_fasta
done
