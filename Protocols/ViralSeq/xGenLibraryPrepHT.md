
# xGen IDT ssDNA & Low-Input DNA Library Prep High-Throughput Protocol

**Objective**: To prepare a viral metagenome or any other sample type that will utilize the xGen IDT ssDNA & Low-Input DNA Library Prep for short-read sequencing on an Illumina platform.

**This is a very long protocol, and mistakes can be very easily made. Please read the protocol in its entirety before proceeding, as many important details may be overlooked!**

## Contents:
- [Intended Use](#intended-use)
- [Materials and Equipment](#materials-and-equipment)
    - [Reagent Handling](#reagent-handling)
    - [Fragmentation](#fragmentation)
    - [Optional Concentration Step](#optional-concentration-step)
- [Protocol Preparations](#protocol-preparations)
- [Protocol](#protocol)
    - [Denaturation](#denaturation)
    - [Adaptase Reaction](#adaptase)
    - [Extension Reaction](#extension)
    - [Ligation Reaction](#ligation)
    - [Indexing PCR](#indexing-pcr)
- [Library QC](#library-qc)
- [Bioinformatic Considertations](#bioinformatic-considerations)
- [Appendix One Thermalcycler Programs](#appendix-one-thermalcycler-programs)
- [Appendix Two Reagent Preparation](#appendix-two-reagent-preparation)
- [Appendix Three Bead Ratios](#appendix-three-bead-ratios)

## Intended Use
The xGen IDT ssDNA & Low-Input DNA Library Prep Kit is suitable for the following sample types:
- Damaged DNA samples
- Samples with a mixture of ssDNA & dsDNA
- Low-input DNA
- Viromes, metagenomes, and phageomes targeting ssDNA & dsDNA bacteriophages
- Ancient DNA Samples

The workflow of this procedure is as follows:
![](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Misc/images/xGen_Workflow.png)

- **Adaptase technology:** Simultaneous tailing and ligation of R2 Stubby Adapter to ssDNA and dsDNA templates.
- **Extension:** Generates the second strand complementary to the template fragments.
- **Ligation:** Adds R1 Stubby Adapter to the original strand.
- **Indexing PCR:** PCR incorporates sample indices and full-length adapters.

The HT version of this protocol was designed to work within a full 96-well Plate. As such, many of the reagent calculations were performed with 96 samples in mind, though per-well reagent volumes are detailed for appropriate calculations.

## Materials and Equipment

### Equipment
- [ ] 96-Well Thermocycler
- [ ] 12.5 µL Integra Mini-96
- [ ] 125 µL Integra Mini-96
- [ ] 10 µL Multi-Channel Pipette
- [ ] 20 µL Multi-Channel Pipette
- [ ] Plate Centrifuge (USA Sci #2532-2000)
- [ ] 96-Well Plate Magnet
- [ ] Agilent TapeStation 4200
- [ ] Plate Vortex (IKA #0003319000)

### Consumables
- [ ] 100% ethanol (200 proof)
- [ ] 50 mL conical tubes
- [ ] 96-well PCR Plates
- [ ] Aerosol-resistant, low retention pipettes and tips, 2 - 1000 µL
- [ ] HSD1000 Sample Buffer (#5067-5603)
- [ ] HSD1000 ScreenTape (#5067-5584)
- [ ] Nuclease-free Water (#10977015)
- [ ] Optical tube 8X strip (Agilent #401428) with cap (#401425)
- [ ] SPRISelect® or AMPure® XP beads (#NC9933872)
- [ ] TapeStation loading tips (Agilent 5067-5599)
- [ ] xGen™ IDT ssDNA & Low-Input DNA Library Prep Kit (#10009817)
- [ ] xGen™ UDI 10nt Primer Plates (#10008052)
- [ ] Plate Seals (#MSB1001)
- [ ] Multichannel Reservoirs (#53504-035)

>[!NOTE]
> Store the xGen ssDNA & Low-Input DNA Library Prep Kit reagents at -20°C, except for the xGen Low EDTA TE Buffer, which is stored at room temperature.

### Reagent Handling
- For non-enzymatic reagents, thaw on ice, then briefly vortex to mix.
- For enzymatic reagents, remove from -20°C and thaw on ice 10 mins before use. 
- When creating master mixes, always include an excess volume of 10%.
- **Be sure to perform pre-PCR and post-PCR processes in the appropriately labeled clean benches.**

This kit accepts DNA from **10 pg to 250 ng**. It is important to know the amount of starting material because the number of PCR cycles run during the Indexing step is dependent upon this number. If using very low-quantity DNA, then use the number of PCR cycles recommended for the lowest input amount.

### Fragmentation
This kit has been specifically designed for use with fragment sizes of 200 bp or 350 bp and has been validated for mechanical shearing (sonication) methods. 

The size of the fragmented library impacts the bead volumes in the subsequent cleanup steps for the extension, ligation, and indexing processes. For this protocol, we will be utilizing **a fragment size of 350 bp.**

### Optional Concentration Step
If you don't have sufficient DNA quantity for the 3 µL starting volume, you will need to concentrate your DNA into a smaller volume. Various options exist, including using the Eppendorf Vacufuge located in the lab.

## Protocol Preparations

**Denaturation Plate**: Ensure fragmented DNA is thawed in a 96-well plate. This plate should **ideally** have at least 15 µL of gDNA to allow for multiple passes in the event of error. The plate should be centrifuged before opening. From the extraction plate, use the Integra mini-96 12.5 µL pipettor to transfer 3 µL of gDNA into a new 96-well plate. Label this plate as *Denaturation Plate*.

**Adaptase Plate**: Assemble the Adapatase Reaction Mixture into a single 1.5 mL microcentrifuge tube. Using a single-channel pipette, evenly distribute the volume of the master mix across 8 0.2 mL PCR strip tubes. Using a multichannel pipette, transfer 5 µL of the Adaptase Reaction Mixture across the 96 wells or into the desired number of wells on the plate. Be sure to leave the plate on ice and **centrifuge before use**. Label this plate as *Adaptase Plate*. 

**Extension Master Mix**: Assemble the Extension Reaction Mixture in a 1.5 mL microcentrifuge tube, **without the W4 enzyme**, and leave on ice until use.

**Post-Extension Cleanup Plates**: Set up 2 96-Well Plates for the double-left-sided selection. Using a multichannel reservoir, pipette 1404 µL of the SPRISelect Beads and dispense into the well. Using a multichannel pipette, transfer 13.92 µL of the SPRISelect Beads from the reservoir across the 96-well plate or the desired number of wells. Label this plate *Extension Bead Cleanup 1*. Using a single-channel pipette, transfer 2420 µL of SPRISelect Beads into the same multi-channel reservoir. Using a multichannel pipette, transfer 24 µL of the SPRISelect Beads from the reservoir across the 96-well plate or the desired number of wells. Label this plate *Extension Bead Cleanup 2*.

**Ligation Master Mix**: Assemble the Ligation Reaction Mixture, **without the B3 enzyme**, and leave on ice until use.

**Post-Ligation Cleanup Plates**: Set up a 96-Well plate for the left-sided selection. Using a multichannel reservoir, pipette 676 µL of the SPRISelect Beads and dispense into the well. Using a multichannel pipette, transfer 6.4 µL of the SPRISelect Beads from the reservoir across the 96-well plate or desired number of wells. Label this plate *Ligation Bead Cleanup*.

**Indexing PCR Plate**: Using the Integra mini-96 12.5 pipette, transfer 1 µL of the xGen UDI Primers to a 96-well plate. Label this plate as *Indexing PCR*. Assemble the Indexing PCR Reaction Mix in a 1.5 mL microcentrifuge tube, **without the W4 enzyme**, and leave on ice until use.

**Post-Indexing PCR Cleanup Plate**: Set up a 96-Well plate for the left-sided selection. Using a multichannel reservoir, pipette 898 µL of the SPRISelect Beads and dispense into the well. Using a multichannel pipette, transfer 8.5 µL of the SPRISelect Beads from the reservoir across the 96-well plate or desired number of wells. Label this plate *Indexing PCR Bead Cleanup*.

**80% Ethanol Preparation**: Create an 80% (vol/vol) solution of 200-proof ethanol and nuclease-free water. **Approximately 500 µL of ethanol will be used per library.** Reserve a 96-well plate for the cleanups for utilization on the Integra Pipettor. 

## Protocol
The starting point for this protocol is post-fragmentation and assumes that you have a sufficient starting amount of DNA for your library. The bead clean-up steps utilize a left-side size selection to remove small fragments and unused adapters.

### Denaturation
1. Start the *Denaturation Program* and preheat the thermocycler to 95°C.
2. Quickly spin down *Denaturation Plate*.
3. Place the **Denaturation Plate** in the thermocycler and run the *Denaturation Program*, detailed in the Appendix.
4. Transfer libraries onto **ice** upon completion of the thermocycling program. Leave for 2 minutes and then proceed with the Adaptase step to preserve the maximum amount of ssDNA substrate.

### Adaptase
1. Make sure the Adaptase thermocycler program is on and that it has reached 37°C before loading the libraries.
2. Quickly spin down *Denaturation Plate* and *Adaptase Plate*.
3. Using the Integra mini-96 12.5 µL pipettor, transfer 3 µL of sheared DNA from the **Denaturation Plate** into the **Adaptase Plate**. 
4. Mix by pipetting or pulse-spin. Spin down.
5. Place the *Adaptase Plate* in the thermocycler and run the *Adaptase Program*, detailed in the Appendix.

### Extension
1. While the Adaptase program runs, ensure that Enzyme W4 is out on ice and is ready to be aliquoted before use in the Extension Master Mix. Be sure to pulse-spin the Extension Master Mix after the addition of Enzyme W4, and briefly spin it down. Keep on ice.
2. Using a PCR strip tube, evenly aliquot the Extension Master Mix amongst the 8 tubes.
3. Using a P20 multichannel pipette, aliquot 9.4 µL of the Extension Master Mix across a new 96-well plate or desired number of wells. Label this plate as the *Extension Plate*. Keep on ice.
4. Once the *Adaptase Program* concludes. Remove samples from the thermocycler and immediately load the *Extension Program*. 
5. Using the Integra mini-96 12.5 µL pipettor, transfer 8 µL from the *Adapatase Plate* to the *Extension Plate*. 
6. Mix by pipetting or pulse-spin. Spin down.
7. With the thermocycler preheated to 98°C. Place the samples in the thermocycler and run the *Extension Program*.
8. Once done with the *Extension Program*, proceed to bead cleanup with SPRISelect or AMPure XP beads.
9. Using the Integra mini-96 125 µL, pipette 17.4 µL from the *Extension Plate* to the *Extension Bead Cleanup 1* plate.
10. Mix by pipetting or pulse-spin. Spin down.
11. Incubate the libraries at room temperature for 5 minutes off-magnet.
12. Place the samples on a magnetic rack until a pellet is formed and the solution clears (~ 2 minutes)
13. Remove and discard the clear supernatant; take care not to remove any beads.
14. Keeping the plate on the magnet, add 125 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
15. Repeat the previous step for a second wash.
16. Quickly spin down.
17. Using the Integra mini-96 12.5 µL pipettor, remove any residual ethanol.
18. Remove libraries from the magnet, and add 22 µL of nuclease-free water to elute.
19. Mix by pipetting or pulse-spin. Spin down.
20. Incubate for 5 minutes to elute DNA off beads.
21. Place on the magnet and wait for the liquid to clear completely for 1-2 minutes. Transfer 20 µL of supernatant into a new 96-well plate.
22. If your input DNA was less than 1 ng, perform a secondary bead cleanup:
    - Transfer 20 µL of supernatant from the previous step (*Extension Bead Cleanup 1*) to the *Extension Bead Cleanup 2* plate.
    - Mix by pipetting or pulse-spin. Spin down.
    - Incubate the libraries at room temperature for 5 minutes off-magnet.
    - Place the samples on a magnetic rack until a pellet is formed and the solution clears (~ 2 minutes)
    - Keeping the plate on the magnet, add 125 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
    - Repeat the previous step for a second wash.
    - Quickly spin down.
    - Using the Integra mini-96 12.5 µL pipettor, remove any residual ethanol.
    - Remove libraries from the magnet, and add 22 µL of nuclease-free water to elute.
    - Mix by pipetting or pulse-spin. Spin down.
    - Incubate for 5 minutes to elute DNA off beads.
    - Place on the magnet and wait for the liquid to clear completely for 1-2 minutes. Using the Integra mini-96 125 µL pipettor, transfer 20 µL of supernatant into a new 96-well plate.
23. Place in a speed vacuum and concentrate at the following specifications:
    - 37°C, 5 PSI, 10 - 20 minutes (Mode: V-AQ)
24. Add 4 µL of low EDTA TE Buffer, vortex to redissolve pellet, and briefly spin down. Label plate as *Post-Extension Plate*.

>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

### Ligation
1. Ensure the Ligation Master Mix is prepared. Add Enzyme B3 just before use.
2. Pulse-vortex the Master Mix, then briefly centrifuge. Keep the Master Mix on ice.
3. Using a PCR strip tube, evenly aliquot the Extension Master Mix amongst the 8 tubes.
4. Using a P20 multichannel pipette, aliquot 4 µL of the Extension Master Mix across a new 96-well plate. Label this plate as the *Ligation Plate*. Keep on ice.
5. Pre-heat the thermocycler to the starting temperature of the *Ligation Program* that was mentioned above.
6. Using the Integra mini-96 12.5 µL pipettor, transfer 4 µL from the *Post-Extension Plate* to the *Ligation Plate*. 
10. Mix by pipetting or pulse-spin. Spin down.
7. Place samples in the pre-heated thermal cycler and run the *Ligation Program*. 
8. Once done with the *Ligation Program*, proceed to bead cleanup with SPRISelect or AMPure XP beads.
9. Using the Integra mini-96 125 µL, pipette 8 µL from the *Ligation Plate* to the *Ligation Bead Cleanup* plate.
10. Mix by pipetting or pulse-spin. Spin down.
11. Incubate the libraries at room temperature for 5 minutes off-magnet.
12. Place the samples on a magnetic rack until a pellet is formed and the solution clears (~ 2 minutes)
13. Remove and discard the clear supernatant; take care not to remove any beads.
14. Keeping the plate on the magnet, add 125 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
15. Repeat the previous step for a second wash.
16. Quickly spin down.
17. Using the Integra mini-96 12.5 µL pipettor, remove any residual ethanol.
18. Remove libraries from the magnet, and add 22 µL of nuclease-free water to elute.
19. Mix by pipetting or pulse-spin. Spin down.
20. Incubate for 5 minutes to elute DNA off beads.
21. Place on the magnet and wait for the liquid to clear completely for 1-2 minutes. Transfer 20 µL of supernatant into a new 96-well plate.
22. Place in a speed vacuum and concentrate at the following specifications:
    - 37°C, 5 PSI, 10 - 20 minutes (Mode: V-AQ)
23. Add 4 µL of low EDTA TE Buffer, vortex to redissolve pellet, and briefly spin down. Label plate as *Post-Ligation Plate*.

>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

### Indexing PCR
1. Preheat the thermal cycler to the starting temperature of the *Indexing PCR Program* as described in the Appendix.
2. Ensure that the Indexing PCR Master Mix is ready. Add Enzyme W4 just before use.
3. Pulse-vortex the Master Mix for 10 seconds, then briefly centrifuge.
4. Using a PCR strip tube, evenly aliquot the Indexing PCR Master Mix amongst the 8 tubes.
5. Using a P20 multichannel pipette, aliquot 5 µL of the Extension Master Mix across the *Indexing PCR Plate*.
6. Mix by pipetting or pulse-spin. Spin down. Keep on ice.
7. Using the Integra mini-96 12.5 µL pipettor, transfer 4 µL from the *Post-Ligation Plate* to the *Indexing PCR Plate*. 
8. Mix by pipetting or pulse-spin. Spin down.
9. Place samples in the pre-heated thermal cycler and run the *Indexing PCR Program*. 
10. Once done with the *Indexing PCR Program*, proceed to bead cleanup with SPRISelect or AMPure XP beads.
11. Using the Integra mini-96 12.5 µL, pipette 10 µL from the *Indexing PCR Plate* to the *Indexing PCR Bead Cleanup* plate.
10. Mix by pipetting or pulse-spin. Spin down.
11. Incubate the libraries at room temperature for 5 minutes off-magnet.
12. Place the samples on a magnetic rack until a pellet is formed and the solution clears (~ 2 minutes)
13. Using the Integra mini-96 125 µL pipettor to remove and discard the clear supernatant; take care not to remove any beads.
14. Keeping the plate on the magnet, add 125 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
15. Repeat the previous step for a second wash.
16. Quickly spin down.
17. Using the Integra mini-96 12.5 µL pipettor, remove any residual ethanol.
18. Remove libraries from the magnet, and add 12 µL of nuclease-free water to elute.
19. Mix by pipetting or pulse-spin. Spin down.
20. Incubate for 5 minutes to elute DNA off beads.
21. Place on the magnet and wait for the liquid to clear completely for 1-2 minutes. Transfer 10 µL of supernatant into a new 96 well plate.

>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

## Library QC

Please refer to QC + Normalization (iSeq) Protocol [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/MetagenomeSeq/iSeq_QC_normalization.md).

## Bioinformatic Considerations
The use of the xGen Adaptase technology in this kit will result in the addition of a low-complexity dinucleotide tail (8 nt in length) to the 3' end. They are observed at the beginning of Read 2 and may be observed towards the end of Read 1. These sequences may need to be removed depending on your computational needs.

## Appendix One Thermalcycler Programs

> [!WARNING]
> Be sure to set the lid temeprature to 105°C for all thermocycler programs **EXCEPT for Ligation Reaction (OFF)**.

### Denaturation

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 95 | 2 min |

### Adaptase

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 37 | 15 min |
| 2 | 95 | 2 min |
| 3 | 4 | Hold |

### Extension

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 98 | 30 sec |
| 2 | 63 | 15 sec |
| 3 | 68 | 5 min |
| 4 | 4 | Hold |

### Ligation

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 25 | 15 min |
| 2 | 4 | Hold |

>[!NOTE]
> The lid temperature for this program will be set to `OFF`

### Indexing PCR

</head>
<body>
    <table>
        <tr>
            <th>Step</th>
            <th>Cycles</th>
            <th>Temperature (°C)</th>
            <th>Time</th>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>98</td>
            <td>30 sec</td>
        </tr>
        <tr>
            <td rowspan="3">2</td>
            <td rowspan="3">Based on sample input (see table below)</td>
            <td>98</td>
            <td>10 sec</td>
        </tr>
        <tr>
            <td>60</td>
            <td>30 sec</td>
        </tr>
        <tr>
            <td>68</td>
            <td>60 sec</td>
        </tr>
        <tr>
            <td>3</td>
            <td>1</td>
            <td>4</td>
            <td>Hold</td>
        </tr>
    </table>
</body>
</html>

| Input (ng) | PCR Cycles |
| :--: | :--: |
| 250 | 3-5 |
| 100 | 4-6 |
| 10 | 7-9 |
| 1 | 10-12 |
| 0.1 | 14-16 |
| 0.01 | 17-19 |

## Appendix Two Reagent Preparation

1. ***Adaptase Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="7">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>2.3μl</td>
        </tr>
        <tr>
            <td>Buffer G1</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent G2</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent G3</td>
            <td>0.5 μl</td>
        </tr>
        <tr>
            <td>Enzyme G4</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td>Enzyme G5</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td>Enzyme G6</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>5 μl</strong></td>
        </tr>
    </table>
</body>
</html>

2. ***Extension Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="4">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>3.7 μl</td>
        </tr>
        <tr>
            <td>Reagent Y1</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td>Reagent W2</td>
            <td>1.4 μl</td>
        </tr>
        <tr>
            <td>Buffer W3</td>
            <td>3.5 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme W4</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>9.4 μl</strong></td>
        </tr>
    </table>
</body>
</html>

3. ***Ligation Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="3">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Buffer B1</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td>Reagent B2</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme B3</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>4 μl</strong></td>
        </tr>
    </table>
</body>
</html>

4. ***Indexing PCR Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="3">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td>Reagent W2</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent W3</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme W4</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>5 μl</strong></td>
        </tr>
    </table>
</body>
</html>

5. ***Ethanol Preparation*** 
- Create an 80% (vol/vol) solution of 200-proof ethanol and nuclease-free water. **Approximately 500 µL of ethanol will be used per library.**

## Appendix Three Bead Ratios

### Extension

<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Number of cleanups</th>
      <th>Sample volume (µL)</th>
      <th>Bead volume (µL)</th>
      <th>Elution volume (µL)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&ge;1 ng, 200 bp</td>
      <td>Single cleanup</td>
      <td>17.4</td>
      <td>20.88 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>&ge;1 ng, 350 bp</td>
      <td>Single cleanup</td>
      <td>17.4</td>
      <td>13.92 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="2">&lt;1 ng, 200 bp</td>
      <td>1st cleanup</td>
      <td>17.4</td>
      <td>20.88 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2nd cleanup</td>
      <td>20</td>
      <td>24 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="2">&lt;1 ng, 350 bp</td>
      <td>1st cleanup</td>
      <td>17.4</td>
      <td>13.92 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2nd cleanup</td>
      <td>20</td>
      <td>24 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
  </tbody>
</table>

### Ligation

| Input | Sample volume (µL) | Bead volume (µL) | Elution volume (µL) |
| :--: | :--: | :---:| :--: |
| All inputs, 200 bp | 8 | 8 (ratio: 1.0x) | 4 |
| All inputs, 350 bp | 8 | 6.4 (ratio: 0.8x) | 4 |

### Indexing PCR

| Input (bp) | Sample volume (µL) | Bead volume (µL) | Elution volume (µL) |
| :--: | :--: | :--: | :--: |
| 200 | 10 | 8.0 (ratio: 0.8x) | 10 |
| 350 | 10 | 8.5 (ratio: 0.85x) | 10 |
