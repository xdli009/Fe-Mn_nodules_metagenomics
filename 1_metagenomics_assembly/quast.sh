for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
quast -t 10 -o ./quast_result/${name} ./megahit_result/${name}.fa
done
