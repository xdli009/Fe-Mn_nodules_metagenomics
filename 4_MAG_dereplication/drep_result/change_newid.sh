for i in `ls ./dereplicated_genomes`
do
name1=${i%%.*}
name2=${i#*.}
cp ./dereplicated_genomes/${i} ./dereplicated_genomes_newid/${name1}_${name2}
done
