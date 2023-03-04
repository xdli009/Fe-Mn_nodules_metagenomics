for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
pullseq -i ./megahit_result/${name}.fasta -m 1000 > ./pullseq_result/${name}_1000bp.fasta
done
