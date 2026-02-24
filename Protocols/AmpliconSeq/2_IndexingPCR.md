# Protocol 2: Indexing PCR

## Theory

While the primary PCR has created the amplicons for sequencing, there is no identifying information on the DNA to tell the sample of origin. This is the purpose of the indexing PCR. In the original Earth Microbiome Project Protocol, a single index/barcode is incorporated onto the reverse (or forward depending on version) primer. Later it became common to put indexes on both sides of the amplicon (dual indexing) where in every combination of forward and reverse barcodes could be used. Unfortunately, due to a phenomenon called barcode/index hopping, this creates a problem on the newest generations of patterned flow cells where in a >3 % of reads may be misassigned to sample of origin (NextSeq/NovaSeq). Alternatively, we are using unique dual indexes (UDIs), i.e. we currently have 574 10nt unique forward, and reverse indexes which are only used one time each per sequencing run in a known combination. These indexes were purchased by the OHMC and are available to use, or for stocks, for members of the center.  

This step essentially involves diluting samples 100x in water before a single limited-cycle PCR which will tack on the remainder of the sequencing adapter. The construct is described in Figure 1. One special note: the nucleotide composition must be relatively balanced at each position of the index. If preparing a sequencing run of less than 96 samples, this should be carefully analysed.

# Materials
- [ ] Primary PCR amplicons in 384 Plate for qPCR (derived from protocol 1). You will need 1 plate for each original plate of gDNA.
- [ ] 384 Plates for qPCR (Biorad #HSP3865 OR Armadillo PCR plate Fisher AB3384)
- [ ] DMSO for PCR (Sigma D8418-50mL)
- [ ] KAPA HiFi PCR kit (KAPA KK2502)
- [ ] Indexing Primer plate at 5µM (Pick 1 of 6 for each plate to be sequenced without overlapping)
- [ ] Nuclease-free H2O (Life Tech 0977-023)
- [ ] Integra Mini-96 12.6 ul pipette
- [ ] 0.5 boxes Integra 12.5 ul sterile nuclease grip tips per 96 well plate to be sequenced (GRIPTIPS 6405)
- [ ] Any multichannel 20 ul pipette with sterile nuclease free tips
- [ ] Any multichannel 100 ul pipette with sterile nuclease free tips
- [ ] Sterile nuclease free reagent reservoir (VistaLab 2138127G)
- [ ] Optically clear Plate Seals (Biorad Microseal ‘B’ #MSB1001)
- [ ] QIAquant 384 or Biorad CFX384.

# Protocol
***Location: in post-PCR area of lab***
- [ ] Obtain a plate of indexes from the freezer and thaw on ice. **Breifly centrifuge before opening!!!!!**
- [ ] In reagent reservoir, prepare master mix according to **Table 1**. Mix well.
- [ ] Using a multichannel or OT2 load 3 µl of master mix into each well of the indexing plate.
- [ ] Using the Mini-96, transfer 2 µl of indexes to the indexing plate. Be sure to use the [template].
- [ ] Store indexing plate while doing water dilutions
- [ ] Using a multichannel load 100 ul water to each well of the dilution plate.
- [ ] Using the Mini-96, transfer 1 ul of gDNA from the primary PCR plate to the dilution plate. Be sure to use this [template](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/96_to_384_Integra.xlsx) to remove the correct wells.
- [ ] Mix gDNA in dilution plate. Note: This can be accomplished with a custom amp dilution program on the Integra.
- [ ] Mix the dilution plate with the Mini-96 and transfer 5 µL from the dilution plate to the indexing plate. Be sure to use the [template].
- [ ] Seal plate with optically clear Plate Seals and briefly centrifuge
- [ ] Transfer to thermocycler and run the program described in Table 2. *Note: we are not using the qPCR capacity of the instrument here, so disregard any warning.*
- [ ] After completion, freeze plates until quantification and pooling.

## Table 1. Indexing PCR Master Mix (3.3x)

Component	            | [Stock] | [Final] | 1 Rxn (10µL rxn) | 96 Rxns|  384 Rxns |   576 rxns|
----------------------|---------|---------|------------------|--------|-----------|-----------|
5x KAPA HiFi Buffer	  | 5x      |  1x     | 2                | 230    |   920     |   1380    |
10 mM dNTPs           | 10mM    |  0.3mM  | 0.3              | 34.5   |   138     |   207     |
DMSO                  |  -      | 0.5%    | 0.5              | 57.5   |   230     |   345     |
KAPA HiFi polymerase  | 1U/µl   | 0.2U/µl | 0.2              | 23     |   92      |   138     |
**Total**	            | -       | -       | **3.0**          | **345**| **1380**  | **2070**  |

## Table 2. Indexing Amplification Parameters
Cycle | Temperature (˚C)	| Time
------|-------------------|------
Initial | Denaturation	95 | 	5 min
10 cycles:
Denature | 98˚C | 20 sec
Anneal | 55˚C | 15 sec
Extend | 72˚C | 30 sec
Holding	| 4˚C	Hold | (0 sec)



***

<img src="https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Misc/images/Fig1.jpg" width="400" height="400">

**Figure 1.** **(A)** Illumina sequencing construct design which allows for an index set to be used for multiple sequencing approaches. **(B)** Distribution of edit distance among newly designed index set (# of sequencing errors required to misidentify barcode). **(C)** Nucleotide composition is balanced at each position of index to maintain base calling accuracy.


