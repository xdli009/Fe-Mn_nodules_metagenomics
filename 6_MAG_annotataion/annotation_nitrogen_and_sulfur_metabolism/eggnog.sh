for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
name=${file%.fa*}
emapper.py -i ../genes_prediction/prodigal_result/${name}_proteins.faa --output ./eggnog_result/${name} -m diamond --cpu 5 --dmnd_db eggnog_proteins.bact_arch.dmnd
done
