for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
workdir=./bwa_result
nt=18
# ******************************************
coverm filter -b ${workdir}/${name}.redup.bam -o ${workdir}/${name}.filter.bam --min-read-percent-identity 95 --min-read-aligned-percent 75 --threads 36
coverm genome -m relative_abundance -b ${workdir}/${name}.filter.bam -s c -o ./abundance/${name} --threads 18
