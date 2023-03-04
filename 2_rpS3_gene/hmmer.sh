for name in A5-S03 A5-S04 KW1-S05 KW1-S08 KW1-S11 KW1-S15 KW1-S21
do
hmmsearch -T 40 --cpu 6 --tblout ./rpS3_fasta/${name}_rpS3.tbl --acc --notextw rpS3_Diamond2019.hmm ../1_metagenomics_assembly/prodigal_result/${name}.faa > ./rpS3_fasta/${name}_rpS3.out
done
