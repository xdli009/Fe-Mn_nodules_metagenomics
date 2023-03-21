for i in `ls *.R`
do
echo ${i}
Rscript ${i}
done
