for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
name=${file%.fa*}
blastp -query ../genes_prediction/prodigal_result/${name}_proteins.faa -out ./blastp_result/${name}.m8 -db ./database/ncyc_scyc_db -outfmt 6 -evalue 1e-20 -num_threads 10
done
