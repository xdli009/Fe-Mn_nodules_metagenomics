for file in `ls ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/`
do
name=${file%.fa*}
tRNAscan-SE -B --thread 5 -b ./trnascan_result/${name}.bed -a ./trnascan_result/${name}.fa ../../4_MAG_dereplication/drep_result/dereplicated_genomes_newid_newcontigid/${file}
done
