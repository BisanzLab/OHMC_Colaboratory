# Protocols and templates for OHMC colaboratory

![](https://psu-gatsby-files-prod.s3.amazonaws.com/s3fs-public/styles/4_3_1500w/public/2023/05/slide1_0.jpeg?h=bd92fb76&itok=QWrXEY_u)

## Project and reagent requests

Please visit this [link](https://forms.gle/QxAVkzP4HyF7zvfQA) to request a project/reagents. Reagents will be allocated on first come/first serve basis and alignment with one health theme.

## Sample shipping

Do not send any samples to lab without first discussing project with Jordan. Please follow [these guidelines](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/0_SampleRequirements.md) when shipping samples. Note: all extracted samples must be sent in full-skirt 96 well plates. Samples to be extracted must be sent in screw top cryovials. A separate sheet with the sample layout is required to protect against damage to labels during shipping.

## Protocol Selection

![](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/flowchart.jpg)

## Nucleic Acid Extraction

<br> [Protocol 1:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Extraction/1_PowerSoil_QiaCubeHT.md) Extraction of gDNA using DNeasy PowerSoil QIAcube HT
<br> [Protocol 1A:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Extraction/1A_PowerSoil_Manual.md) Alternate protocol: Extraction of gDNA using DNeasy PowerSoil Individual Columns
<br> [Protocol 2:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Extraction/2_RNeasy_QiaCubeHT.md) Extraction of total RNA using RNeasy QIAcube HT


## Amplicon Sequencing

<br> [Protocol 1:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/1_PrimaryPCR.md) Primary PCR
<br> [Optional Protocol 1.5:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/1.5_BeadCleanup.md) PCR Cleanup before indexing (for samples with significant dimer formation)
<br> [Protocol 2:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/2_IndexingPCR.md) Indexing PCR
<br> [Protocol 3:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/3_Pooling.md) Pooling
<br> [Protocol 4:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/4_Cleanup.md) Size selection and cleanup
<br> [Considerations for ITS](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/ITS_Amplification_Considerations.md)

## Metagenomic Sequencing

<br> [Protocol 1:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/MetagenomeSeq/IlluminaPrep_HTP.md) High throughput Illumina DNA Prep
<br> [Protocol 1A:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/MetagenomeSeq/IlluminaPrep_Individual.md) Alternate protocol: Scaled Illumina DNA prep in strip tubes
<br> [Protocol 2:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/MetagenomeSeq/iSeq_QC_normalization.md) QC + Normalization with iSeq

## Virome Sequencing

<br> [Protocol 1:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/ViralSeq/VLPEnrichment.md) VLP enrichment by filtration
<br> [Protocol 2:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/ViralSeq/QIAmpMinEluteViral.md) QIAamp MinElute Viral DNA extraction
<br> [Protocol 3:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/ViralSeq/xGenLibraryPrep.md) Scaled xGen ssDNA and Low Input DNA Library Prep
<br> [Protocol 4:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/ViralSeq/QIAseqWholeViromeLibraryPrep.md) QIAseq Whole Virome Library Prep
 
## Library QC and Sequencing

<br> [Protocol 1:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Sequencing/LibraryQC_Tapestation.md) Library QC By Tapestation D1000
<br> [Protocol 2:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Sequencing/LibraryQuant_NebNext.md) Library Quantification by NebNext qPCR
<br> [Protocol 3:](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Sequencing/NextSeq2000.md) Loading P1 600 cycle kits on NextSeq 2000

## Data Analysis

<br> [V4 16S rRNA denoising and processing](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/analysis_scripts/AmpliconSeq_q2.Rmd)
<br> [Fast quality control of shallow metagenomic sequencing using Kraken](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/analysis_scripts/QC_iSeq_MGS.sh)
<br> [Metagenomic processing on ROAR cluster with fastp, metaphlan, humann, and optional metaspades assembly](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/analysis_scripts/mgs_humann_pipeline.sh)
<br> [Simple cross sectional MGS analysis using outputs of previous script](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/analysis_scripts/MGS_analysis_template.Rmd)

