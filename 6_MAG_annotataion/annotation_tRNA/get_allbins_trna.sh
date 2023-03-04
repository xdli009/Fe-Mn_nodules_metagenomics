echo "id,tRNA number" >> allbins_trna.csv
for i in `ls ./trnascan_result/*.bed`
do
name1=`basename ${i}`
name2=${name1%.bed*}
num=`cat ${i} | wc -l`
echo "${name2},${num}" >> allbins_trna.csv
done
