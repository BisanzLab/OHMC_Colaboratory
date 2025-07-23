#MGS QC Pipeline
#jb 1 feb 2025
# run fastp on each sample, then tries to generate shallow taxonomic composition for sanity check and flag potential issues

conda activate kraken2

NTHREADS=8
READDIR=/data/SequencingRuns/2025July02_Pecan/iseq_qc/OHMC-425835412/FASTQ_Generation_2025-07-23_13_04_34Z-841652826/


################# FastP
mkdir -p read_qc
for R1 in $(ls -1 ${READDIR}/*/*R1_001.fastq.gz); do
	sampleid=$(basename $R1 | sed 's/_S[0-9].*//g')
	R2=$(echo $R1 | sed 's/_R1_/_R2_/g')
    echo "Processing $sampleid, forward $R1, reverse $R2"

/data/shared_resources/sftwr/fastp_0.23.2/fastp \
 --in1 $R1 \
 --in2 $R2 \
 --out1 read_qc/${sampleid}_R1.fastq.gz \
 --out2 read_qc/${sampleid}_R2.fastq.gz \
 --trim_poly_g \
 --html read_qc/${sampleid}_report.html \
 --json read_qc/${sampleid}_report.json \
 --thread $NTHREADS

done

multiqc read_qc
################


################# Kraken
mkdir -p kraken2_qc
for R1 in $(ls -1 ${READDIR}/*/*R1_001.fastq.gz); do
	sampleid=$(basename $R1 | sed 's/_S[0-9].*//g')
	R2=$(echo $R1 | sed 's/_R1_/_R2_/g')
    echo "Processing $sampleid, forward $R1, reverse $R2"

kraken2 \
 --db /data/shared_resources/databases/kraken2/kraken2_standard_20220607 \
 --threads $NTHREADS \
 --quick \
 --report-minimizer-data \
 --report kraken2_qc/${sampleid}.report \
 --output kraken2_qc/${sampleid}.kraken2 \
 --use-names \
 read_qc/${sampleid}_R1.fastq.gz \
 read_qc/${sampleid}_R2.fastq.gz

bracken \
 -d /data/shared_resources/databases/kraken2/kraken2_standard_20220607 \
 -i kraken2_qc/${sampleid}.report \
 -l S \
 -r 150 \
 -t $NTHREADS \
 -o kraken2_qc/${sampleid}.species_abundances \
 -w kraken2_qc/${sampleid}.bracken

done
################

