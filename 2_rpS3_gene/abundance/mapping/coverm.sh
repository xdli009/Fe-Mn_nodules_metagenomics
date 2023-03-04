for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
workdir=./mapping_result
nt=36
# ******************************************
coverm filter -b ${workdir}/${name}.redup.bam -o ${workdir}/${name}.filter.bam --min-read-percent-identity 99 --min-read-aligned-percent 75 --threads ${nt}
coverm contig --methods mean -b ${workdir}/${name}.filter.bam -o ${workdir}/${name} --threads ${nt}
rm ${workdir}/${name}.sort.bam
rm ${workdir}/${name}.redup.bam
rm ${workdir}/${name}.redup.metrics.txt
done
