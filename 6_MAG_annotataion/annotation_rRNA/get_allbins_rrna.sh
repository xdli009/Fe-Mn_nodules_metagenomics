echo "id,rRNA number" >> allbins_rrna.csv
for i in `ls ./barrnap_result/*.gff`
do
name1=`basename ${i}`
name2=${name1%_rRNA*}
num=`cat ${i} | wc -l`
a=$(($num-1))
echo "${name2},${a}" >> allbins_rrna.csv
done
