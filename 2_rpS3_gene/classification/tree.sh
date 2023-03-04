file_fasta="rpS3_centroid_and_ref.fasta"
out=${file_fasta%.*}
nt=36

mafft --auto --thread $nt ${file_fasta} > ${out}.phy
trimal -in ${out}.phy -out ${out}.trim_0.05.phy -gt 0.05
iqtree -s ${out}.trim_0.05.phy -m TEST -alrt 1000 -bb 1000 -nt $nt
