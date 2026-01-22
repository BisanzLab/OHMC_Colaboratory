#!/bin/bash
#SBATCH --job-name humann_bisanz
#SBATCH --nodes=1
#SBATCH --ntasks=18
#SBATCH --mem=128GB
#SBATCH --array=1-130 # the number of input files for parallel processing. This would do 130 samples from the manifest starting with the first. Note that the headerline is not counted.
#SBATCH --output humann_pipeline.log
#SBATCH --error humann_pipeline.err
#SBATCH --partition=sla-prio
#SBATCH --account=one_sc_default
#SBATCH --time=48:00:00 #change as needed
#SBATCH --mail-type=START,END,FAIL
#SBATCH --mail-user=jpb6325@psu.edu

######################################################################################################################################################################################
# Metagenome Pipeline v0.011 JB
# Notes:
# -if interactive session is needed: salloc --nodes=1 --ntasks=4 --mem=32G --time=03:00:00
# --array=1-2 which lines of the file to go through. This would do the first two samples (note the headerline is not counted)
# -on ROAR large files should go on the scratch directory, but will be cleared off after 30 days. It would be ideal to stage the results here but return the final files to work or home
# -Can also use account=open amd remove partition line, as SBATCH --account=open
# - this script can also assemble; however, may required longer than 48h. Recommend to set RunMicrobeCensus, RunMetaphlan, and RunHumann to false for assembly.
######################################################################################################################################################################################

######################################################################################################################################################################################
# Change log:
# - 30 Apr 2025 - initial setup and debugging
# - 28 July 2025 - changed handling of postqc reads, added explicit polyG removal assuming all data will be novaseq/nextseq, although this would have been occurring by default
#
#
#
#
#
######################################################################################################################################################################################

#/storage/work/jpb6325/conda_roar is install location
#created humann_30Apr2025 environment with humann, kneaddata, fastp, and metaspades. Microbecensus and MetaSpades  are in own environments due to python conflict

# Load humann environment from JB's work directory. This is humann 3.9
#humann_config --update database_folders nucleotide /storage/work/jpb6325/humann_databases/chocophlan/
#humann_config --update database_folders protein /storage/work/jpb6325/humann_databases/uniref/
#humann_config --update database_folders utility_mapping /storage/work/jpb6325/humann_databases/utility_mapping/

source /storage/work/jpb6325/conda_roar/etc/profile.d/conda.sh
conda activate humann_30Apr2025

######################################################################################################################################################################################
# Tasks -> set true or false as desired
RunFastP=true # do QC on reads
RemoveHost=true #Note: adjust as needed below, defaulting to mouse host
HostSpecies="mouse" # can be mouse or human which controls reference genome for removing host reads
KeepQCReads=true # should the QC reads be kept? This might not be preferable for storage reasons, depends on application. Be sure to store the reads somewhere with sufficient storage (i.e. not home directory)
RunMicrobeCensus=true # calculate genome equivalent calculations
RunMetaplan=true # Should metaphlan be run? 
RunHumann=true # Should metaphlan be run? Note: do not have this be true if humann is also running as they will be redundant
RunMetaSpades=false # Should assembly be done?



######################################################################################################################################################################################
#Input/Putput parameters -> be sure to use absolute file paths for cluster
OutDir="/storage/home/jpb6325/MGS2_processed/output"
Reads="/scratch/jpb6325/reads/" # a directory containing all fastq files to be processed with no subdirectory structure. This will be the absolute path prefix for the files listed in the manfiest
QCReads="/scratch/jpb6325/qcreads/" # this is optional
Manifest="/storage/home/jpb6325/MGS2_processed/MGS2_processing_manifest.tsv" # a tsv file with the following columns: SampleID, Lib1_F, Lib1_R, Lib2_F, Lib2_R where F and R are the forward and reverse reads, and lib1 and lib2 are if the sample was sequenced multiple times

#Example Manifest
#SampleID	Lib1_F	Lib1_R	Lib2_F	Lib2_R
#McReynolds1_C1_Control	C1_control_CKDN250003824-1A_22THGKLT4_L5_1.fq.gz	C1_control_CKDN250003824-1A_22THGKLT4_L5_2.fq.gz		
#McReynolds1_C2_Control	C2_control_CKDN250003825-1A_22TGMMLT4_L4_1.fq.gz	C2_control_CKDN250003825-1A_22TGMMLT4_L4_2.fq.gz	C2_control_CKDN250003825-1A_22THGKLT4_L5_1.fq.gz	C2_control_CKDN250003825-1A_22THGKLT4_L5_2.fq.gz
#McReynolds1_C3_Control	C3_control_CKDN250003826-1A_22THGHLT4_L3_1.fq.gz	C3_control_CKDN250003826-1A_22THGHLT4_L3_2.fq.gz	C3_control_CKDN250003826-1A_22THGKLT4_L5_1.fq.gz	C3_control_CKDN250003826-1A_22THGKLT4_L5_2.fq.gz


######################################################################################################################################################################################
# Do not modify below this line

#Set up directories and logs
mkdir -p $OutDir
mkdir -p $OutDir/logs

WorkDir=$(mktemp -d -p /scratch/${USER}) # putting temp working files on scratch to avoid storage overruns. The folder name is randomly generated
JobID=$SLURM_JOB_ID
ArrayID=$(expr $SLURM_ARRAY_TASK_ID + 1)
Nthreads=$SLURM_NPROCS 
MemReq=$SLURM_MEM_PER_NODE

#Test settings for interactive node
#JobID=1
#ArrayID=2
#Nthreads=4
#MemReq=32

SampleID=$(sed "${ArrayID}q;d" ${Manifest} | cut -f 1)
R1_L1=$(sed "${ArrayID}q;d" ${Manifest} | cut -f 2)
R2_L1=$(sed "${ArrayID}q;d" ${Manifest} | cut -f 3)
R1_L2=$(sed "${ArrayID}q;d" ${Manifest} | cut -f 4)
R2_L2=$(sed "${ArrayID}q;d" ${Manifest} | cut -f 5)
LibNumber=$(if [ "$R2_L2" = "" ]; then echo 1; else echo 2; fi) # to know if there are multiple libraries

echo $(date) Running on $SampleID with $LibNumber lanes and files: $R1_L1 $R2_L1 $R1_L2 $R2_L2 outputing to $OutDir/${SampleID} and temporary storage in $WorkDir >> $OutDir/logs/MGS_MasterLog.txt # dump starts to a master log
exec > ${OutDir}/logs/${SampleID}.log 2> ${OutDir}/logs/${SampleID}.err # move each sample to it's own log
echo $(date) Running on $SampleID 
echo Number of threads: $Nthreads 
echo Memory Usage: $MemReq
echo Number of Libraries: $LibNumber 
echo Reads: $R1_L1 $R2_L1 $R1_L2 $R2_L2 
echo Output directory:  $OutDir
echo Temporary directory: $WorkDir
echo Job ID: $JobID
echo Array ID: $ArrayID


#############################################################################################################################################################################################
# Move reads to temp directory
mkdir -p $WorkDir/reads
cp $Reads/${R1_L1} $WorkDir/reads/${SampleID}_L1_R1.fastq.gz
cp $Reads/${R2_L1} $WorkDir/reads/${SampleID}_L1_R2.fastq.gz
if [ "$LibNumber" == "2" ]; then
	cp $Reads/${R1_L2} $WorkDir/reads/${SampleID}_L2_R1.fastq.gz
	cp $Reads/${R2_L2} $WorkDir/reads/${SampleID}_L2_R2.fastq.gz
fi

#############################################################################################################################################################################################
# QC via FastP
if $RunFastP; then
	echo $(date) Starting fastp
	for i in $(seq 1 $LibNumber); do
		mkdir -p $WorkDir/fastpout
		mkdir -p ${OutDir}/fastp
		fastp \
		--in1 $WorkDir/reads/${SampleID}_L${i}_R1.fastq.gz \
		--in2 $WorkDir/reads/${SampleID}_L${i}_R2.fastq.gz \
		--out1 $WorkDir/fastpout/${SampleID}_L${i}_1.fastq.gz \
		--out2 $WorkDir/fastpout/${SampleID}_L${i}_2.fastq.gz \
		--detect_adapter_for_pe \
		--trim_poly_g \
		--cut_front \
		--cut_tail \
		--cut_window_size 4 \
		--cut_mean_quality 20 \
		--length_required 60 \
		--json $OutDir/fastp/${SampleID}_L${i}.json \
		--html $OutDir/fastp/${SampleID}_L${i}.html \
		--thread $Nthreads
		
		mv $WorkDir/fastpout/${SampleID}_L${i}_1.fastq.gz $WorkDir/reads/${SampleID}_L${i}_R1.fastq.gz
		mv $WorkDir/fastpout/${SampleID}_L${i}_2.fastq.gz $WorkDir/reads/${SampleID}_L${i}_R2.fastq.gz
	done
fi


#############################################################################################################################################################################################
# Remove Host Reads using KneadData (bowtie2)
#Note databases are /storage/work/jpb6325/humann_databases/hosts/Homo_sapiens_hg39_T2T_Bowtie2_v0.1/bowtie2-index/ and /storage/work/jpb6325/humann_databases/hosts/mouse_C57BL_6NJ_Bowtie2_v0.1

if [ "$HostSpecies" == "mouse" ]; then 
	KNDB=/storage/work/jpb6325/humann_databases/hosts/mouse_C57BL_6NJ_Bowtie2_v0.1
elif [ "$HostSpecies" == "human" ]; then
	KNDB=/storage/work/jpb6325/humann_databases/hosts/Homo_sapiens_hg39_T2T_Bowtie2_v0.1/bowtie2-index/
fi

if $RemoveHost; then
	echo $(date) Starting hostgenome removal
	for i in $(seq 1 $LibNumber); do
		kneaddata \
		--bypass-trim \
		--bypass-trf \
		--remove-intermediate-output \
		--threads $Nthreads \
		--scratch $WorkDir \
		-db $KNDB \
		--input1 $WorkDir/reads/${SampleID}_L${i}_R1.fastq.gz \
		--input2 $WorkDir/reads/${SampleID}_L${i}_R2.fastq.gz \
		--output $WorkDir/hosttrim \
		--output-prefix $SampleID
		
		pigz -p $Nthreads -c $WorkDir/hosttrim/${SampleID}_paired_1.fastq > $WorkDir/reads/${SampleID}_L${i}_R1.fastq.gz
		pigz -p $Nthreads -c $WorkDir/hosttrim/${SampleID}_paired_2.fastq > $WorkDir/reads/${SampleID}_L${i}_R2.fastq.gz
	 done
	 
fi

#############################################################################################################################################################################################
#Move Reads if needed
if $KeepQCReads; then
	mkdir -p $QCReads
	for i in $(seq 1 $LibNumber); do
		cp $WorkDir/reads/${SampleID}_L${i}_R1.fastq.gz ${QCReads}/${SampleID}_L${i}_R1.fastq.gz
		cp $WorkDir/reads/${SampleID}_L${i}_R2.fastq.gz ${QCReads}/${SampleID}_L${i}_R2.fastq.gz
	done
fi

#############################################################################################################################################################################################
# Merge reads if needed
if [ "$LibNumber" == "2" ]; then
	echo $(date) Merging Reads
	zcat $WorkDir/reads/${SampleID}_L1_R1.fastq.gz $WorkDir/reads/${SampleID}_L1_R1.fastq.gz > $WorkDir/reads/${SampleID}_R1.fastq
	zcat $WorkDir/reads/${SampleID}_L2_R1.fastq.gz $WorkDir/reads/${SampleID}_L2_R2.fastq.gz > $WorkDir/reads/${SampleID}_R2.fastq

else
	echo $(date) Renaming Reads
	zcat $WorkDir/reads/${SampleID}_L1_R1.fastq.gz > $WorkDir/reads/${SampleID}_R1.fastq
	zcat $WorkDir/reads/${SampleID}_L1_R2.fastq.gz > $WorkDir/reads/${SampleID}_R2.fastq
fi

cat $WorkDir/reads/${SampleID}_R1.fastq $WorkDir/reads/${SampleID}_R2.fastq > $WorkDir/reads/${SampleID}_humann.fastq

#############################################################################################################################################################################################
# Microbecensus -> requires python 2.7 so in own environment
if $RunMicrobeCensus; then
	conda activate microbecensus
	echo $(date) Starting copy number estimations
	mkdir -p ${OutDir}/microbecensus
	run_microbe_census.py -v -t $Nthreads $WorkDir/reads/${SampleID}_R1.fastq,$WorkDir/reads/${SampleID}_R2.fastq ${OutDir}/microbecensus/${SampleID}.microbecensus
	conda deactivate
fi

#############################################################################################################################################################################################
# Metaphlan v 4.0.6
# database is stored within the conda environment #/storage/work/jpb6325/.conda/envs/humann_30Apr2025/lib/python3.7/site-packages/metaphlan/metaphlan_databases/

if $RunMetaphlan; then
	echo $(date) Starting metaphlan
	mkdir -p ${OutDir}/metaphlan
	#export DEFAULT_DB_FOLDER=/storage/work/jpb6325/humann_databases/metaphlan4
	metaphlan $WorkDir/reads/${SampleID}_humann.fastq $OutDir/metaphlan/${SampleID}.metaphlan \
	--bowtie2out $WorkDir/${SampleID}.bowtie2.bz2 \
	--input_type fastq \
	--add_viruses \
	--unclassified_estimation \
	--sample_id $SampleID \
	--nproc $Nthreads \
	--tmp_dir $WorkDir/metaphlan_scratch
fi

#############################################################################################################################################################################################
# Humann
if $RunHumann; then
	echo $(date) Starting Humann
	cat $WorkDir/reads/${SampleID}_R1.fastq $WorkDir/reads/${SampleID}_R2.fastq > $WorkDir/reads/${SampleID}_humann.fastq
	mkdir -p $WorkDir/humann
	humann \
	--input $WorkDir/reads/${SampleID}_humann.fastq \
	--output $WorkDir/humann/$SampleID \
	--threads $Nthreads \
	--input-format fastq \
	--search-mode uniref90 \
	--verbose \
	--output-basename $SampleID
	
	mkdir -p $OutDir/humann
	cp $WorkDir/humann/${SampleID}/*tsv $OutDir/humann/
	cp $WorkDir/humann/${SampleID}/${SampleID}_humann_temp/${SampleID}_metaphlan_bugs_list.tsv $OutDir/humann/
	
fi

#############################################################################################################################################################################################
# Assemble with metaspades v 4.1.0
# needs own conda environment for python 3.8
if $RunMetaSpades; then
	conda activate python3.8
	echo $(date) Starting assembly
	mkdir -p $WorkDir/assemblytmp
	mkdir -p $WorkDir/assemblies
	mkdir -p $OutDir/assemblies
	if [ "$LibNumber" == "2" ]; then
		/storage/home/jpb6325/work/SPAdes-4.1.0-Linux/bin/spades.py --meta \
		--threads $Nthreads \
		--memory $MemReq \
		--tmp-dir $WorkDir/assemblytmp \
		--pe-1 1 $WorkDir/reads/${SampleID}_L1_R1.fastq.gz \
		--pe-2 1 $WorkDir/reads/${SampleID}_L1_R2.fastq.gz \
		--pe-1 2 $WorkDir/reads/${SampleID}_L2_R1.fastq.gz \
		--pe-2 2 $WorkDir/reads/${SampleID}_L2_R1.fastq.gz \
		-o $WorkDir/assemblies/$SampleID
	else
		/storage/home/jpb6325/work/SPAdes-4.1.0-Linux/bin/spades.py --meta \
		--threads $Nthreads \
		--memory $MemReq \
		--tmp-dir $WorkDir/assemblytmp \
		-1 $WorkDir/reads/${SampleID}_R1.fastq \
		-2 $WorkDir/reads/${SampleID}_R2.fastq \
		-o $WorkDir/assemblies/$SampleID
	fi
	cp $WorkDir/assemblies/${SampleID}/scaffolds.fasta $OutDir/assemblies/${SampleID}_scaffolds.fasta
	conda deactivate
fi

#############################################################################################################################################################################################
echo $(date) Finished $SampleID 
rm -r $WorkDir

