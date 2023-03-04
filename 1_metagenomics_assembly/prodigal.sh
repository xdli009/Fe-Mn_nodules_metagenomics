for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
prodigal -i ./pullseq_result/${name}_1000bp.fasta -f gff -o ./prodigal_result/${name}.gff -a ./prodigal_result/${name}.faa -d ./prodigal_result/${name}.ffn -p meta
done
