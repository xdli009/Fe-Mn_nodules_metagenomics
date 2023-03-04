for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
fq1=${name}_1.fq.gz
fq2=${name}_2.fq.gz
fasta=../index/allbins.fa
nt=32
bwa mem -t $nt $fasta $fq1 $fq2 | samtools view -@ $nt -bS | samtools sort -@ $nt -o ./result/${name}.sort.bam
coverm genome -m relative_abundance -b ./${name}.sort.bam -s c -o ./result/${name}_rb_sort.txt --threads $nt
done
