# Amplicon Sequencing Protocol 1- Primary PCR

## Theory
This protocol and the subsequent indexing steps were originally derived from a “Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies” [doi:10.1038/nbt.3601](https://www.nature.com/articles/nbt.3601). The methods have been heavily modified to optimize throughput and minimize cost while also adapting to our equipment and supplies.

The preparation of the amplicons is carried out in two steps (primary and indexing) for two main reasons: 1) it is more cost effective as it allows the same set of expensive dual unique indexes to be used for multiple targets and/or amplicon and metagenomic sequencing, and 2) it allows for the primary PCR to be conducted as a qPCR reaction which allows for real time monitoring of successful reaction and negates the need to run gels to verify amplification which is time consuming and expensive. Furthermore, qPCR is being carried out in 384 well plates which allows for heavily reduced reaction volumes and higher throughputs. Potentially an entire sequencing run can be prepared in a day.

Limiting amplification cycles helps prevent against over-amplification, and thus massive amounts of reads lost to chimeras and other technical artifacts (>20%), the primary PCR is carried out as a quantitative PCR that provides real-time feed back on amplification. The downside is that primer dimers that occur after cycle 25 may mask amplicons in low biomass samples. If studying low biomass samples (ex skin), 30-35 cycles of PCR should be run, and amplicons inspected by gel electrophoresis or similar method. Careful consideration of bacterial biomass and/or extent of host contamination should be considered and a pilot run should be carried out for non standard sample types (ex. feces).

Another advantage of this amplification strategy is that you can mix and match 16S variable regions and metagenomic sequencing (see **Table 1**). A list of primers is attached below however it is reccomended to use V4_515Fmod_Nextera and V4_806Rmod_Nextera which are the revised EMP V4 primers. It is also possible to sequence multiple variable regions or combine 16S rRNA and ITS into a single run so long as the indexes do not overlap.

Before progressing, it is imperative that you have accurately captured the layout of your 96 well plate(s). Please use [this template](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/Amplicon_RunTemplate.xlsx) which will allow for seemless transition into sequencing. Be sure to enquire about which index plate you will use.

Note: the mini-96 and multichannels pipette every other well.  See [this template](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/96_to_384_Integra.xlsx) to understand the layout.

## Materials

- [ ] 384 Plates for qPCR (Biorad #HSP3865 OR Armadillo PCR plate Fisher AB3384)
- [ ] gDNA from in a standard 96 well plate or Qiagen Capture plate
- [ ] Integra Mini-96 12.6 ul pipette
- [ ] 1 box Integra 12.5 ul sterile nuclease grip tips (GRIPTIPS 6405)
- [ ] Any multichannel 10 ul pipette with sterile nuclease free tips
- [ ] QIAquant 384 or Biorad CFX384
- [ ] Sterile nuclease free reagent reservoir (VistaLab 2138127G)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)
- [ ] DMSO for PCR (Sigma D8418-50mL)
- [ ] SYBR Green I (Sigma S9430 - 10,000x stock) - diluted 10x in DMSO to 1000x
- [ ] KAPA HiFi Hot Start PCR kit (KAPA KK2502)
- [ ] PCR primers of choice at 100µM (see **Table 1**)
- [ ] Nuclease-free H2O (Life Tech 0977-023)


## Protocol
***Location:** PCR hood or separate room/area from other steps*
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat PCR area with UV light for ~15 minutes.
- [ ] Generate enough PCR master mix for the number of samples you will be preparing in reagent reservoir (see **Table 2**). Mix well with a 1000ul pipette and/or rocking reservoir.
- [ ] Using 10 ul multichannel, transfer 9 ul of master mix into each well of qPCR plate which will be loaded. Be sure to consider the [96-to-384 well layout](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/96_to_384_Integra.xlsx).
NOTE: if using the pre-PCR OT-2 for mastermix, keep in mind the selection of plate 1 (aliquots FULL plate) vs plate 2 (aliquots 1/2 plate, every other column) in the setup.
- [ ] Thaw gDNA plate on ice and briefly centrifuge to prevent cross contamination. **This centrifugation is essential.**
- [ ] Load gDNA on to Mini-96 and transfer 1 ul to qPCR plate
- [ ] Cover 384 well plate with optically clear plate seals
- [ ] Briefly centrifuge qPCR plate and transfer to qPCR instrument
- [ ] Run qPCR as indicated in **Table 3**.

## QC
A successful amplification curve should had formed for all samples, and no curves should be observed for negative controls (**Figure 2**). Optionally, a 1% agarose gel can be used to spot check some amplifications. Sporadic failures can be diluted 10x and attempted again which will correct issues encountered with potential wash buffer carry over.

## Figures

![fig1](https://github.com/jbisanz/AmpliconSeq/blob/master/images/ampcurves.png)

**Figure 2**. qPCR amplification curves for a single sample shows dilution series. Note that the extraction blanks have not amplified. Amplification may be observed at 25 cycles of PCR due to primer dimers in negative controls. See protocols for low biomass samples for more information and recommendations.

## Tables

**Table 1. Primers for primary PCR**
**Primer name** | **Marker gene** | **Target region** | **Sequence**
----------------|-----------------|-------------------|---------------
V4_515Fmod_Nextera | 16S rRNA | V4 |         TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*GTGYCAGCMGCCGCGGTAA*
V4_806Rmod_Nextera | 16S rRNA | V4 |         GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*GGACTACNVGGGTWTCTAAT*
V1_27F_Nextera | 16S rRNA | V1-V3 |          TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*AGAGTTTGATCMTGGCTCAG*
V3_534R_Nextera | 16S rRNA | V1-V3 |         GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*ATTACCGCGGCTGCTGG*
V3_357F_Nextera | 16S rRNA | V3-V4, V3-V5 |  TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*CCTACGGGAGGCAGCAG*
V4_515F_Nextera | 16S rRNA | V4, V4-V6 |     TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*GTGCCAGCMGCCGCGGTAA*
V4_806R_Nextera | 16S rRNA | V3-V4, V4 |     GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*GGACTACHVGGGTWTCTAAT*
V5F_Nextera  | 16S rRNA | V5-V6 |            TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*RGGATTAGATACCC*
V5_926R_Nextera | 16S rRNA | V3-V5 |         GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*CCGTCAATTCMTTTRAGT*
V6R_Nextera | 16S rRNA | V5-V6, V4-V6 |      GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*CGACRRCCATGCANCACCT*
18S_V9_1391_F_Nextera | 18S rRNA | V9 |      TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*GTACACACCGCCCGTC*
18S_V9_EukBr_R_Nextera | 18S rRNA | V9 |     GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*TGATCCTTCTGCAGGTTCACCTAC*
ITS1F_Nextera | ITS | ITS1 |                 TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*CTTGGTCATTTAGAGGAAG\*TAA*
ITS2_Nextera | ITS | ITS1 |                  GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*GCTGCGTTCTTCATCGA\*TGC*
5.8SR_Nextera | ITS | ITS2 |                 TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG*TCGATGAAGAACGCAGCG*
ITS4_Nextera | ITS | ITS2 |                  GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG*TCCTCCGCTTATTGATATGC*

**Table 2. Primary PCR Master Mix**
| Component                    | Reaction Concentration | 1 Rxn (µL) | 96 Rxns (ul) | 384 Rxns (µL) | 574 Rxns (µL)
|------------------------------|------------------------|------------|--------------|---------------|--------------
| Nuclease-free H2O            | -                      |    5.955   | 655.05       |  2,501.1      |  3,751.7
| 5x KAPA HiFi Buffer          | 1x                     |     2      |    220       |   840         |  1,260
| 10 mM dNTPs                  | 0.3 mM                 |  0.3       | 33           |   126         |  189
| DMSO                         | 0.50%                  | 0.5        | 55           | 210           | 315
| 1000x SYBR Green             | 0.005%                 | 0.005      | 0.55         | 2.1           | 3.15
| 100 µM Forward Primer        | 200 nM                 | 0.02       | 2.2          | 8.4           | 12.6
| 100 µM Reverse Primer        | 200 nM                 | 0.02       | 2.2          | 8.4            | 12.6
| KAPA HiFi polymerase (1U/µL) | 0.2 U                  | 0.2        | 22           | 84            | 126
| Total                        | -                      | 9          | 990          | 3,780         | 5,760

\**Note: calculations pad for reagent loss in reservoire

**Table 3. Primary PCR Amplification Parameters**
Cycle |	Temperature (˚C)  | Time
------|-------------------|------
Initial Denaturation   |	95	| 5 min
23 cycles\*:
Denature | 98˚C | 20 sec
Anneal | 55˚C	| 15 sec
Extend | 72˚C | 30 sec
Holding	| 4˚C	Hold | 0 sec

\**25 cycles is a good starting point here. With V4 primers, primer dimers will occur after cycle 25 and will make judging the success of amplification difficult without running gel or secondary QC.*


