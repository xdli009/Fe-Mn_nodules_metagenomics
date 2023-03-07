for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
name=${file%.fa*}
prodigal -i ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/${file} -f gff -o ./prodigal_result/${name}_genes.gff -a ./prodigal_result/${name}_proteins.faa -d ./prodigal_result/${name}_cds.ffn
done
