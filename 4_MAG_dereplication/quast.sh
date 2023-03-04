for file in `ls ./drep_result/dereplicated_genomes_newid_newcontigid`
do
name=${file%.fa*}
quast -t 12 -o ./MAGs_quast/${name}/ ./drep_result/dereplicated_genomes_newid_newcontigid/${file}
done
