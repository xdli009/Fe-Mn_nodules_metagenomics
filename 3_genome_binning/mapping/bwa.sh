for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
fq1=${name}_1.fq.gz
fq2=${name}_2.fq.gz
fasta=../index/${name}_fasta
workdir=./bwa_result
nt=28
bwa mem -t $nt $fasta $fq1 $fq2 | samtools view -@ $nt -bS | samtools sort -@ $nt \
-m 3000000000 -o ${workdir}/${name}.sort.bam
java -jar picard.jar MarkDuplicates REMOVE_DUPLICATES=true I=${workdir}/${name}.sort.bam O=${workdir}/${name}.redup.bam M=${workdir}/${name}.redup.metrics.txt
done
