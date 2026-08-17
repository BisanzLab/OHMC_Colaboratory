# PowerSoil Manual

## Theory

To effectively characterize a microbial community requires even lysis of all of its members. Some organisms like *E. coli* break open if you look at them the wrong way. Others like *E. lenta* require considerably more effort. Gram-positive organisms in stationary phase growth can be >90% peptidoglycan (cell wall) by weight. To ensure even lysis, mechanical lysis is preferred using shaking with beads at a high occurrence.

This protocol uses the current iteration of the PowerSoil reagents (previously MoBio). This will ensure even lysis of communities, and isolation of high purity DNA with little residual PCR inhibitors which will cause problems in down stream enzymatic reactions (like those needed for sequencing or qPCR).


All extractions  MUST include at least one blank tube labeled Extraction Control (ExtCon). It is ideal to include a positive control such as the Zymo Community.

A template has been provided to track sample layouts in 96 well plates. Download [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/0_ExtractionPlate_Template.xlsx). Please utilize it to ensure smooth integration into later workflows. Print a copy and keep in your lab book as well as a copy in the Sequencing Run log book. If samples will be submitted to the collaboratory, they must be arrayed in 96-well full skirted plates and follow these [naming conventions](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/0_SampleRequirements.md).

## Materials

- [ ] PowerSoil Pro kit, Qiagen #47014
- [ ] Tissuelyzer III or similar (MPBio FastPrep 96)
- [ ] Single/multichannel pipettes capable of 200-1000ul volumes and appropriate tips

## Preparation
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat area with UV light for ~15 minutes.
- [ ] Bring buffer CD2 out of fridge.
- [ ] Make sure that there is no precipitate in CD3 (SDS). If there is, heat in water bath until dissolved.
- [ ] All tubes can be set up and labeled ahead of time as shown:

![](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Misc/images/Tube_rack_PS.jpeg)

  ## Sample Disruption

*Location: If samples are BSL2, conduct all work in Biosafety Cabinet, if BSL1, conduct all work in PCR cabinet.

- [ ] Briefly spin bead tubes to bring beads to bottom. Add up to 250mg of material and 800ul of CD1, vortex.
- [ ] Transfer tubes to bead beater (MPBio in BLS2 room or TissueLyser). Note: unit must be balanced. 
- [ ] Tighten ratchet(s) until they will no longer move.
- [ ] Run for 5 minutes at 25 Hz.
- [ ] Centrifuge tubes at 15,000g x 1min.

## DNA Extraction
*Location: DNA extraction hood

- [ ] While samples spin, aliquot 200ul/tube CD2 into the next row of microcentrifuge tubes.
- [ ]	Recover supernatant from power bead tubes and transfer to the corresponding tube containing CD2. Vortex 5sec to mix. (Note: avoid the pelleted beads/particles and pipet slowly; approximate recovery is around 400-500ul)
- [ ]	Centrifuge tubes at 15,000g x 1min.
- [ ]	While samples spin, aliquot 600ul/tube CD3 into the next row of microcentrifuge tubes.
- [ ]	Recover supernatant from tubes and transfer to the corresponding tube containing CD3. Vortex 5sec to mix. (Note: avoid the pellet and pipet slowly; approximate recovery is around 500-700ul)
- [ ]	Load up to 650ul each lysate onto a spin column.
- [ ] Centrifuge at 15,000g x 1min.
- [ ] Discard flow-through; load any remaining lysate to column.
- [ ] Centrifuge at 15,000g x 1min.
- [ ] Discard flow-through and collection tube; place each column in a new collection tube.
- [ ]	Add 500ul EA; Centrifuge at 15,000g x 1min.
- [ ]	Discard flow-through and re-use same collection tube.
- [ ]	Add 500ul C5; Centrifuge at 15,000g x 1min.
- [ ]	Discard flow-through and collection tube; place each column in a new collection tube.
- [ ]	Centrifuge at 15,000g x 2min to remove any residual wash buffer.
- [ ]	Place columns into elution tubes; Add 50ul DNase/RNase free water directly to the center of the membrane.
- [ ]	Centrifuge at 15,000g x 1min; Discard columns.
- [ ]	Depending on downstream applications, it may be desirable to array DNA samples in a 96-well PCR plate. 
- [ ]	Quantitate DNA by Qubit or Nanodrop and store at -20C.
