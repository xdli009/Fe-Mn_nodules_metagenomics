for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
megahit -t 36 -1 ${name}_1.fq.gz -2 ${name}_2.fq.gz -o ./megahit_result/${name}
done
