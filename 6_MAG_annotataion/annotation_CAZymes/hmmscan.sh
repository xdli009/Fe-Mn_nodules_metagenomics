for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
namenew=${file%.fa*}
hmmscan -E 1e-14 --domE 1e-14 --cpu 30 --noali --acc --notextw --tblout ${namenew}.tbl --domtblout ./dom_tbl/${namenew}_dom.tbl dbCAN-HMMdb-V8.txt ../genes_prediction/prodigal_result/${name}_proteins.faa
done
