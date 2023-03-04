for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
name=${file%.fa*}
barrnap --kingdom arc --lencutoff 0.2 --reject 0.3 --evalue 1e-05 --threads 12 --outseq ./barrnap_result/${name}_rRNA.fa ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/${file} > ./barrnap_result/${name}_rRNA.gff
done
