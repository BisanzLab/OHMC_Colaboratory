# Considerations for ITS Amplification

This document provides guidance for adapting the [OHMC Primary PCR protocol](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/1_PrimaryPCR.md) for amplification of fungal Internal Transcribed Spacer (ITS) regions from diverse sample types (e.g., human fecal, plant foliar). ITS targets may require higher cycle numbers, additional cleanup steps, and appropriate positive controls to ensure successful library generation.

---

## General Considerations

- **Cycle number:** ITS amplicons may require up to **35 cycles** to achieve sufficient yield.  
  A test run on a subset of samples is recommended to determine the appropriate cycle number for each sample type.

- **Positive controls:** Include a DNA control known to reliably amplify ITS under these conditions.  
  - ZymoBIOMICS Microbial Community Standard (#D6305) contains only **two fungal species**.  
  - A better option is the ATCC Mycobiome Genomic DNA Mix (#MSA-1010), which includes **ten fungal species**.

- **No-template control (NTC):** Always include an NTC to detect contamination and primer-dimer formation.

- **Amplicon characteristics:** ITS regions are often:
  - lower in abundance than 16S rRNA,
  - longer and more variable in size,
  - more challenging to amplify consistently.

  These differences may necessitate increased cycle numbers and additional purification steps.

---

## Cleanup and Size Selection

If amplification requires **>23 cycles**, perform **[Protocol 1.5 – Bead Cleanup](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/1.5_BeadCleanup.md)** prior to indexing to remove primer dimers

Primer dimers should be assessed by analyzing representative samples and the NTC on the **TapeStation**. Removing primer dimers before indexing is critical, as indexed dimers will occupy the flow cell and drastically reduce sequencing depth.

### Library Pool Behavior

ITS libraries typically produce **multiple bands** on an agarose gel due to amplicon size variability (≈200–800 bp). After pooling:

- Purify the pool **twice** using 0.6× AMPure beads: **[Protocol 4 – Cleanup](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/4_Cleanup.md)**
- Analyze the final pool on the TapeStation to verify:
  - insert-size distribution  
  - concentration before sequencing

---

## ITS Amplification From Maize Foliar Samples

The PCR cycling temperatures and times from the [OHMC Primary PCR protocol](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/AmpliconSeq/1_PrimaryPCR.md) are suitable using **33 cycles** with the following primers from [White et al., 1990](https://www.researchgate.net/publication/223397588_White_T_J_T_D_Bruns_S_B_Lee_and_J_W_Taylor_Amplification_and_direct_sequencing_of_fungal_ribosomal_RNA_Genes_for_phylogenetics):

- **ITS1F:**  
  5'-(TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG)CTTGGTCATTTAGAGGAAGTAA-3'

- **ITS2:**  
  5'-(GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG)GCTGCGTTCTTCATCGATGC-3'


---

## ITS Amplification From Human Fecal Samples

Adapted from [Hoggard, et al, 2018](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02208/full)
Amplification of ITS from human fecal DNA is often inconsistent with the KAPA HiFi enzyme.  
A more reliable protocol uses **Platinum SuperFi II (ThermoFisher #12368010)**.

### PCR Master Mix Setup (9 µL reaction volume)

| Component | Reaction Concentration | 1 Rxn (µL) | 48 Rxns (µL) | 96 Rxns (µL) | 384 Rxns (µL) | 432 Rxns (µL) | 574 Rxns (µL) |
|----------|-------------------------|------------|--------------|--------------|----------------|----------------|----------------|
| Nuclease-free H₂O | — | 3.955 | 237.3 | 435.05 | 1661.1 | 1898.4 | 2531.2 |
| 2× SuperFi II Platinum Taq | 1× | 5.0 | 300 | 550 | 2100.0 | 2400.0 | 3200.0 |
| 1000× SYBR Green | 0.01% | 0.005 | 0.3 | 0.55 | 2.1 | 2.4 | 3.2 |
| 100 µM Forward Primer | 200 nM | 0.02 | 1.2 | 2.2 | 8.4 | 9.6 | 12.8 |
| 100 µM Reverse Primer | 200 nM | 0.02 | 1.2 | 2.2 | 8.4 | 9.6 | 12.8 |
| **Total** | — | **9 µL** | — | **990 µL** | **3780 µL** | **4320.0 µL** | **5760 µL** |

### Primers (White et al., 1990)

- **White_ITS2_F:**  
  5'-(TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG)GCATCGATGAAGAACGCAGC-3'

- **White_ITS2_R:**  
  5'-(GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG)TCCTCCGCTTATTGATATGC-3'
  
### Thermocycler Program
Cycle |	Temperature (˚C)  | Time
------|-------------------|------
Initial Denaturation   |	95	| 15 min
33 cycles\*:
Denature | 95˚C | 30 sec
Anneal | 52˚C	| 30 sec
Extend | 70˚C | 60 sec
'
Final Extension | 70˚C | 7 min
Hold	| 4˚C | 

