from opentrons import protocol_api
import csv
import numpy

# metadata
metadata = {
    'protocolName': 'PoolEquimolar', 
    'author': 'J Bisanz, jordan.bisanz@gmail.com',
    'description': 'Cherry picking protocol to generate equimolar pools of amplicon libraries. All volumes are transferred to a single 1.5mL Eppendorf tube',
    'apiLevel': '2.7'
}


#fix disposing first tip, and protocol comment instead of print, add tip touch on both sides?

# The data below is taken from a the tracking sheet
# Note: Ensure that total volumes to be transferred do not exceed 1.4mL!!!!! If so, program will pause and ask you to replace the tube when it is full. After run merge all tubes.
# Lines 17-114 are to be replaced with the users data taken from the loadings.csv of the tracking sheet.
loadings = '''
sampleid,plate96,well96,plate384,well384,flag,volume
EOSC_241,Plate1,A1,Plate1,A1,.,2.891476246
EOSC_221,Plate1,B1,Plate1,C1,.,3.562851008
EOSC_182,Plate1,C1,Plate1,E1,.,2.954872304
EOSC_34,Plate1,D1,Plate1,G1,.,3.597716314
EOSC_155,Plate1,E1,Plate1,I1,.,4.669098645
EOSC_55,Plate1,F1,Plate1,K1,.,4.156205152
EOSC_165,Plate1,G1,Plate1,M1,.,5.305487306
EOSC_279,Plate1,H1,Plate1,O1,X,10
EOSC_243,Plate1,A2,Plate1,A3,.,3.313736997
EOSC_ExtCon_Plate1B2,Plate1,B2,Plate1,C3,.,3.854394839
EOSC_217,Plate1,C2,Plate1,E3,.,4.382426295
EOSC_96,Plate1,D2,Plate1,G3,.,8.556947771
EOSC_171,Plate1,E2,Plate1,I3,.,4.644809124
EOSC_128,Plate1,F2,Plate1,K3,.,3.496331125
EOSC_88,Plate1,G2,Plate1,M3,X,10
EOSC_24,Plate1,H2,Plate1,O3,.,2.281833344
EOSC_82,Plate1,A3,Plate1,A5,.,3.14491023
EOSC_59,Plate1,B3,Plate1,C5,.,6.317753963
EOSC_114,Plate1,C3,Plate1,E5,.,3.702550428
EOSC_106,Plate1,D3,Plate1,G5,.,5.04479526
EOSC_43,Plate1,E3,Plate1,I5,.,4.0959417
EOSC_164,Plate1,F3,Plate1,K5,.,3.614883342
EOSC_170,Plate1,G3,Plate1,M5,.,5.127308507
EOSC_4,Plate1,H3,Plate1,O5,.,3.273814298
EOSC_132,Plate1,A4,Plate1,A7,.,3.660267178
EOSC_146,Plate1,B4,Plate1,C7,.,4.699378413
EOSC_75,Plate1,C4,Plate1,E7,X,10
EOSC_113,Plate1,D4,Plate1,G7,.,4.587701016
EOSC_173,Plate1,E4,Plate1,I7,.,3.384964192
EOSC_183,Plate1,F4,Plate1,K7,.,3.206833377
EOSC_3,Plate1,G4,Plate1,M7,.,4.523779473
EOSC_108,Plate1,H4,Plate1,O7,.,3.442647727
EOSC_264,Plate1,A5,Plate1,A9,X,10
EOSC_116,Plate1,B5,Plate1,C9,.,2.850106352
EOSC_263,Plate1,C5,Plate1,E9,.,6.372507473
EOSC_188,Plate1,D5,Plate1,G9,.,5.150282673
EOSC_176,Plate1,E5,Plate1,I9,.,4.032516601
EOSC_249,Plate1,F5,Plate1,K9,.,4.58685929
EOSC_129,Plate1,G5,Plate1,M9,.,6.008745128
EOSC_1,Plate1,H5,Plate1,O9,.,3.643065552
EOSC_42,Plate1,A6,Plate1,A11,.,3.680474457
EOSC_227,Plate1,B6,Plate1,C11,X,10
EOSC_57,Plate1,C6,Plate1,E11,.,6.333358878
EOSC_101,Plate1,D6,Plate1,G11,.,4.800443177
EOSC_124,Plate1,E6,Plate1,I11,.,3.115127965
EOSC_94,Plate1,F6,Plate1,K11,.,6.138204121
EOSC_231,Plate1,G6,Plate1,M11,.,2.347064679
EOSC_73,Plate1,H6,Plate1,O11,.,3.278429475
EOSC_233,Plate1,A7,Plate1,A13,.,3.870207184
EOSC_228,Plate1,B7,Plate1,C13,.,3.480390263
EOSC_225,Plate1,C7,Plate1,E13,.,3.678714333
EOSC_ZymoCom_Plate1D7,Plate1,D7,Plate1,G13,.,3.024948871
EOSC_262,Plate1,E7,Plate1,I13,.,3.7477874
EOSC_153,Plate1,F7,Plate1,K13,.,4.005542068
EOSC_91,Plate1,G7,Plate1,M13,.,9.599314993
EOSC_206,Plate1,H7,Plate1,O13,.,2.937943868
EOSC_27,Plate1,A8,Plate1,A15,.,2.821478562
EOSC_198,Plate1,B8,Plate1,C15,X,10
EOSC_194,Plate1,C8,Plate1,E15,.,3.960959202
EOSC_143,Plate1,D8,Plate1,G15,X,10
EOSC_38,Plate1,E8,Plate1,I15,.,4.008753514
EOSC_209,Plate1,F8,Plate1,K15,X,10
EOSC_285,Plate1,G8,Plate1,M15,.,3.36514404
EOSC_268,Plate1,H8,Plate1,O15,.,2.470452767
EOSC_45,Plate1,A9,Plate1,A17,.,2.942612292
EOSC_13,Plate1,B9,Plate1,C17,.,4.424111229
EOSC_185,Plate1,C9,Plate1,E17,.,3.68128739
EOSC_99,Plate1,D9,Plate1,G17,.,4.49288574
EOSC_229,Plate1,E9,Plate1,I17,.,5.440575047
EOSC_257,Plate1,F9,Plate1,K17,X,10
EOSC_123,Plate1,G9,Plate1,M17,.,4.42391551
EOSC_11,Plate1,H9,Plate1,O17,X,10
EOSC_147,Plate1,A10,Plate1,A19,.,3.104200884
EOSC_175,Plate1,B10,Plate1,C19,.,3.239872725
EOSC_70,Plate1,C10,Plate1,E19,X,10
EOSC_19,Plate1,D10,Plate1,G19,X,10
EOSC_282,Plate1,E10,Plate1,I19,X,10
EOSC_72,Plate1,F10,Plate1,K19,.,7.627526523
EOSC_ExtCon_Plate1G10,Plate1,G10,Plate1,M19,.,4.059362493
EOSC_2,Plate1,H10,Plate1,O19,.,3.622609576
EOSC_212,Plate1,A11,Plate1,A21,.,2.905928414
EOSC_230,Plate1,B11,Plate1,C21,.,2.858334374
EOSC_56,Plate1,C11,Plate1,E21,.,2.793888425
EOSC_53,Plate1,D11,Plate1,G21,.,2.684101877
EOSC_255,Plate1,E11,Plate1,I21,.,5.331794933
EOSC_276,Plate1,F11,Plate1,K21,.,3.97686894
EOSC_32,Plate1,G11,Plate1,M21,.,3.309240956
EOSC_29,Plate1,H11,Plate1,O21,.,2.860214728
EOSC_281,Plate1,A12,Plate1,A23,.,4.019549481
EOSC_238,Plate1,B12,Plate1,C23,.,3.244919025
EOSC_95,Plate1,C12,Plate1,E23,.,2.60964352
EOSC_283,Plate1,D12,Plate1,G23,.,2.910919178
EOSC_121,Plate1,E12,Plate1,I23,.,3.913372031
EOSC_187,Plate1,F12,Plate1,K23,.,2.877995166
EOSC_189,Plate1,G12,Plate1,M23,.,2.981567058
EOSC_117,Plate1,H12,Plate1,O23,.,2.618458404
EOSC_177,Plate2,A1,Plate1,B1,.,6.861812026
EOSC_184,Plate2,B1,Plate1,D1,.,3.991472618
EOSC_66,Plate2,C1,Plate1,F1,X,10
EOSC_169,Plate2,D1,Plate1,H1,X,10
EOSC_210,Plate2,E1,Plate1,J1,.,3.908172027
EOSC_51,Plate2,F1,Plate1,L1,.,3.907255813
EOSC_6,Plate2,G1,Plate1,N1,.,7.401699874
EOSC_179,Plate2,H1,Plate1,P1,.,4.27416001
EOSC_78,Plate2,A2,Plate1,B3,.,7.607796774
EOSC_54,Plate2,B2,Plate1,D3,.,3.441107679
EOSC_149,Plate2,C2,Plate1,F3,.,3.358137657
EOSC_211,Plate2,D2,Plate1,H3,.,8.915508616
EOSC_195,Plate2,E2,Plate1,J3,.,2.211293029
EOSC_79,Plate2,F2,Plate1,L3,.,7.429746178
EOSC_261,Plate2,G2,Plate1,N3,.,4.571133929
EOSC_235,Plate2,H2,Plate1,P3,.,3.370929308
EOSC_120,Plate2,A3,Plate1,B5,.,4.603116955
EOSC_136,Plate2,B3,Plate1,D5,.,4.846978466
EOSC_15,Plate2,C3,Plate1,F5,.,8.02735079
EOSC_ExtCon_Plate2D3,Plate2,D3,Plate1,H5,.,5.590836842
EOSC_14,Plate2,E3,Plate1,J5,.,3.624185057
EOSC_162,Plate2,F3,Plate1,L5,.,1.934969169
EOSC_250,Plate2,G3,Plate1,N5,.,5.675558943
EOSC_277,Plate2,H3,Plate1,P5,.,6.287168957
EOSC_193,Plate2,A4,Plate1,B7,X,10
EOSC_90,Plate2,B4,Plate1,D7,.,3.884036648
EOSC_216,Plate2,C4,Plate1,F7,X,10
EOSC_65,Plate2,D4,Plate1,H7,.,2.455047467
EOSC_22,Plate2,E4,Plate1,J7,.,8.450649475
EOSC_265,Plate2,F4,Plate1,L7,.,2.814886584
EOSC_159,Plate2,G4,Plate1,N7,X,10
EOSC_74,Plate2,H4,Plate1,P7,.,3.943775953
EOSC_139,Plate2,A5,Plate1,B9,.,8.370715554
EOSC_5,Plate2,B5,Plate1,D9,.,2.931914209
EOSC_214,Plate2,C5,Plate1,F9,X,10
EOSC_222,Plate2,D5,Plate1,H9,.,6.771668153
EOSC_251,Plate2,E5,Plate1,J9,.,6.419140336
EOSC_254,Plate2,F5,Plate1,L9,.,5.724291776
EOSC_186,Plate2,G5,Plate1,N9,.,3.169530919
EOSC_166,Plate2,H5,Plate1,P9,.,4.146382219
EOSC_224,Plate2,A6,Plate1,B11,.,6.421201265
EOSC_64,Plate2,B6,Plate1,D11,X,10
EOSC_133,Plate2,C6,Plate1,F11,.,2.187398354
EOSC_93,Plate2,D6,Plate1,H11,.,6.317753963
EOSC_144,Plate2,E6,Plate1,J11,.,5.679427014
EOSC_63,Plate2,F6,Plate1,L11,.,4.295456996
EOSC_49,Plate2,G6,Plate1,N11,.,6.186430559
EOSC_84,Plate2,H6,Plate1,P11,.,5.839617248
EOSC_163,Plate2,A7,Plate1,B13,.,2.770819173
EOSC_47,Plate2,B7,Plate1,D13,.,4.429206007
EOSC_26,Plate2,C7,Plate1,F13,.,2.389177409
EOSC_245,Plate2,D7,Plate1,H13,.,4.669752751
EOSC_68,Plate2,E7,Plate1,J13,.,2.127143177
EOSC_213,Plate2,F7,Plate1,L13,.,7.110650973
EOSC_28,Plate2,G7,Plate1,N13,.,4.990914041
EOSC_199,Plate2,H7,Plate1,P13,.,4.877237494
EOSC_83,Plate2,A8,Plate1,B15,.,5.429939929
EOSC_138,Plate2,B8,Plate1,D15,.,5.692358748
EOSC_12,Plate2,C8,Plate1,F15,.,5.032862073
EOSC_157,Plate2,D8,Plate1,H15,.,7.936879584
EOSC_41,Plate2,E8,Plate1,J15,.,5.880827385
EOSC_151,Plate2,F8,Plate1,L15,.,2.681151319
EOSC_142,Plate2,G8,Plate1,N15,.,6.143106114
EOSC_172,Plate2,H8,Plate1,P15,.,3.353970313
EOSC_125,Plate2,A9,Plate1,B17,.,5.778539775
EOSC_256,Plate2,B9,Plate1,D17,.,5.660139205
EOSC_247,Plate2,C9,Plate1,F17,.,2.862343326
EOSC_174,Plate2,D9,Plate1,H17,.,8.461375092
EOSC_80,Plate2,E9,Plate1,J17,X,10
EOSC_205,Plate2,F9,Plate1,L17,.,5.590836842
EOSC_271,Plate2,G9,Plate1,N17,.,5.437912364
EOSC_135,Plate2,H9,Plate1,P17,X,10
EOSC_131,Plate2,A10,Plate1,B19,.,2.732359138
EOSC_ZymoCom_P2B10,Plate2,B10,Plate1,D19,.,2.699462618
EOSC_126,Plate2,C10,Plate1,F19,.,6.117176972
EOSC_97,Plate2,D10,Plate1,H19,.,4.355133243
EOSC_208,Plate2,E10,Plate1,J19,.,3.17023429
EOSC_178,Plate2,F10,Plate1,L19,.,6.886857878
EOSC_ExtCon_Plate2G10,Plate2,G10,Plate1,N19,X,10
EOSC_275,Plate2,H10,Plate1,P19,X,10
EOSC_61,Plate2,A11,Plate1,B21,.,3.864523711
EOSC_248,Plate2,B11,Plate1,D21,.,5.962172401
EOSC_52,Plate2,C11,Plate1,F21,X,10
EOSC_9,Plate2,D11,Plate1,H21,.,8.596670853
EOSC_40,Plate2,E11,Plate1,J21,X,10
EOSC_110,Plate2,F11,Plate1,L21,.,7.041058525
EOSC_154,Plate2,G11,Plate1,N21,.,5.751618649
EOSC_200,Plate2,H11,Plate1,P21,.,9.792966887
EOSC_204,Plate2,A12,Plate1,B23,.,8.000377618
EOSC_107,Plate2,B12,Plate1,D23,.,6.484070907
EOSC_253,Plate2,C12,Plate1,F23,.,5.827027033
EOSC_286,Plate2,D12,Plate1,H23,.,3.955006267
EOSC_112,Plate2,E12,Plate1,J23,.,5.270256098
EOSC_46,Plate2,F12,Plate1,L23,.,4.050155506
EOSC_220,Plate2,G12,Plate1,N23,.,3.232228159
EOSC_87,Plate2,H12,Plate1,P23,.,5.755591125
EOSC_181,Plate3,A1,Plate1,A2,X,10
EOSC_48,Plate3,B1,Plate1,C2,.,5.432889955
EOSC_134,Plate3,C1,Plate1,E2,.,2.036518441
EOSC_39,Plate3,D1,Plate1,G2,.,3.744980322
EOSC_21,Plate3,E1,Plate1,I2,.,3.162014342
EOSC_180,Plate3,F1,Plate1,K2,.,7.456337551
EOSC_37,Plate3,G1,Plate1,M2,.,3.050602479
EOSC_109,Plate3,H1,Plate1,O2,.,4.342085095
EOSC_267,Plate3,A2,Plate1,A4,.,3.149565628
EOSC_218,Plate3,B2,Plate1,C4,.,3.505523478
EOSC_ExtCon_Plate3C2,Plate3,C2,Plate1,E4,.,3.1853819
EOSC_119,Plate3,D2,Plate1,G4,.,2.906857597
EOSC_36,Plate3,E2,Plate1,I4,.,3.181530832
EOSC_273,Plate3,F2,Plate1,K4,.,2.673624507
EOSC_191,Plate3,G2,Plate1,M4,.,2.605563765
EOSC_219,Plate3,H2,Plate1,O4,X,10
EOSC_223,Plate3,A3,Plate1,A6,.,3.352059053
EOSC_17,Plate3,B3,Plate1,C6,.,2.296295089
EOSC_272,Plate3,C3,Plate1,E6,.,2.29766688
EOSC_270,Plate3,D3,Plate1,G6,X,10
EOSC_44,Plate3,E3,Plate1,I6,.,3.753695983
EOSC_86,Plate3,F3,Plate1,K6,.,2.529698022
EOSC_102,Plate3,G3,Plate1,M6,.,2.452157789
EOSC_20,Plate3,H3,Plate1,O6,.,2.346568999
EOSC_192,Plate3,A4,Plate1,A8,.,3.263237896
EOSC_150,Plate3,B4,Plate1,C8,.,2.388264451
EOSC_67,Plate3,C4,Plate1,E8,.,2.279129035
EOSC_236,Plate3,D4,Plate1,G8,.,2.063540114
EOSC_190,Plate3,E4,Plate1,I8,.,2.836926916
EOSC_30,Plate3,F4,Plate1,K8,.,2.773201225
EOSC_23,Plate3,G4,Plate1,M8,.,2.609303053
EOSC_81,Plate3,H4,Plate1,O8,.,3.031735296
EOSC_89,Plate3,A5,Plate1,A10,.,3.467597555
EOSC_258,Plate3,B5,Plate1,C10,.,2.310994719
EOSC_100,Plate3,C5,Plate1,E10,.,2.218160032
EOSC_35,Plate3,D5,Plate1,G10,.,2.59044473
EOSC_284,Plate3,E5,Plate1,I10,.,2.315543246
EOSC_232,Plate3,F5,Plate1,K10,.,1.913714077
EOSC_130,Plate3,G5,Plate1,M10,.,1.979202148
EOSC_33,Plate3,H5,Plate1,O10,.,2.24555554
EOSC_31,Plate3,A6,Plate1,A12,.,3.10999331
EOSC_69,Plate3,B6,Plate1,C12,.,4.067618462
EOSC_239,Plate3,C6,Plate1,E12,.,2.524652601
EOSC_140,Plate3,D6,Plate1,G12,.,3.06509558
EOSC_141,Plate3,E6,Plate1,I12,.,2.363540404
EOSC_148,Plate3,F6,Plate1,K12,.,3.198832042
EOSC_158,Plate3,G6,Plate1,M12,.,4.840643593
EOSC_242,Plate3,H6,Plate1,O12,.,3.811061301
EOSC_246,Plate3,A7,Plate1,A14,.,4.018741804
EOSC_207,Plate3,B7,Plate1,C14,.,3.941599682
EOSC_92,Plate3,C7,Plate1,E14,.,5.297617502
EOSC_50,Plate3,D7,Plate1,G14,.,1.852626867
EOSC_127,Plate3,E7,Plate1,I14,X,10
EOSC_ExtCon_Plate3D7,Plate3,F7,Plate1,K14,.,4.504218426
EOSC_105,Plate3,G7,Plate1,M14,.,2.489394557
EOSC_168,Plate3,H7,Plate1,O14,.,3.693388207
EOSC_252,Plate3,A8,Plate1,A16,.,3.657723411
EOSC_58,Plate3,B8,Plate1,C16,X,10
EOSC_161,Plate3,C8,Plate1,E16,.,4.058044647
EOSC_156,Plate3,D8,Plate1,G16,X,10
EOSC_104,Plate3,E8,Plate1,I16,.,3.508352159
EOSC_16,Plate3,F8,Plate1,K16,.,4.396104875
EOSC_7,Plate3,G8,Plate1,M16,.,3.038090669
EOSC_237,Plate3,H8,Plate1,O16,.,9.519811203
EOSC_98,Plate3,A9,Plate1,A18,X,10
EOSC_278,Plate3,B9,Plate1,C18,X,10
EOSC_ZymoCom_P3C9,Plate3,C9,Plate1,E18,X,10
EOSC_203,Plate3,D9,Plate1,G18,X,10
EOSC_244,Plate3,E9,Plate1,I18,X,10
EOSC_137,Plate3,F9,Plate1,K18,X,10
EOSC_240,Plate3,G9,Plate1,M18,X,10
EOSC_8,Plate3,H9,Plate1,O18,X,10
EOSC_111,Plate3,A10,Plate1,A20,.,3.2547411
EOSC_234,Plate3,B10,Plate1,C20,.,2.182052574
EOSC_10,Plate3,C10,Plate1,E20,.,2.489642465
EOSC_76,Plate3,D10,Plate1,G20,.,2.798814758
EOSC_259,Plate3,E10,Plate1,I20,.,2.730046703
EOSC_197,Plate3,F10,Plate1,K20,.,2.608758489
EOSC_25,Plate3,G10,Plate1,M20,.,3.390817869
EOSC_260,Plate3,H10,Plate1,O20,.,2.956095187
EOSC_122,Plate3,A11,Plate1,A22,.,4.628470369
EOSC_71,Plate3,B11,Plate1,C22,.,2.389748362
EOSC_103,Plate3,C11,Plate1,E22,.,2.023168926
EOSC_145,Plate3,D11,Plate1,G22,.,2.335280412
EOSC_202,Plate3,E11,Plate1,I22,.,2.242131855
EOSC_274,Plate3,F11,Plate1,K22,.,2.39295075
EOSC_62,Plate3,G11,Plate1,M22,.,2.634323497
EOSC_167,Plate3,H11,Plate1,O22,.,2.729152617
EOSC_201,Plate3,A12,Plate1,A24,.,4.305443674
EOSC_115,Plate3,B12,Plate1,C24,.,2.844027017
EOSC_269,Plate3,C12,Plate1,E24,.,2.20811921
EOSC_18,Plate3,D12,Plate1,G24,.,2.901038891
EOSC_196,Plate3,E12,Plate1,I24,.,2.529442073
EOSC_60,Plate3,F12,Plate1,K24,.,2.63842427
EOSC_215,Plate3,G12,Plate1,M24,.,4.63447652
EOSC_226,Plate3,H12,Plate1,O24,.,2.771126305
EOSC_85,Plate4,A1,Plate1,B2,.,3.884036648
EOSC_266,Plate4,B1,Plate1,D2,.,6.9206978
EOSC_ZymoCom_P4C1,Plate4,C1,Plate1,F2,.,2.732807159
EOSC_243_rep,Plate4,D1,Plate1,H2,.,5.368721079
EOSC_152,Plate4,E1,Plate1,J2,.,4.019549481
EOSC_ExtCon_Plate4F1,Plate4,F1,Plate1,L2,.,5.843712253
EOSC_160,Plate4,G1,Plate1,N2,.,8.668959317
EOSC_77,Plate4,H1,Plate1,P2,.,4.277633835
EOSC_44_rep,Plate4,A2,Plate1,B4,X,10
EOSC_ExtCon_Plate4B2,Plate4,B2,Plate1,D4,.,5.426698597
EOSC_280,Plate4,C2,Plate1,F4,.,3.611358589
EOSC_241_rep,Plate4,D2,Plate1,H4,.,6.187196093
EOSC_ExtCon_Plate4E2,Plate4,E2,Plate1,J4,.,5.5131624
EOSC_ExtCon_Plate4F2,Plate4,F2,Plate1,L4,.,3.655316786
EOSC_ZymoDNA_P4G2,Plate4,G2,Plate1,N4,X,10
EOSC_ZymoDNA_P4H2,Plate4,H2,Plate1,P4,X,10
Anderson_Human_BZH08_01,Plate4,A3,Plate1,B6,.,2.535213481
Anderson_Human_BZH64_01,Plate4,B3,Plate1,D6,.,2.223387772
Anderson_Mouse_BZH64_01,Plate4,C3,Plate1,F6,.,9.390191569
Anderson_Mouse_BZH64_02,Plate4,D3,Plate1,H6,.,6.315758892
Anderson_Mouse_BZH64_03,Plate4,E3,Plate1,J6,.,2.024110803
Anderson_Mouse_BZH64_04,Plate4,F3,Plate1,L6,.,3.509460277
Anderson_Mouse_BZH64_05,Plate4,G3,Plate1,N6,.,4.9589867
Anderson_Mouse_BZH64_06,Plate4,H3,Plate1,P6,.,2.647995825
Anderson_Mouse_BZH64_07,Plate4,A4,Plate1,B8,.,3.916437327
Anderson_Mouse_BZH64_08,Plate4,B4,Plate1,D8,.,2.105244986
Anderson_Mouse_BZH64_09,Plate4,C4,Plate1,F8,.,3.109316414
Anderson_Mouse_BZH64_10,Plate4,D4,Plate1,H8,X,10
Anderson_Mouse_BZH08_01,Plate4,E4,Plate1,J8,.,2.602580042
Anderson_Mouse_BZH08_02,Plate4,F4,Plate1,L8,.,2.265395115
Anderson_Mouse_BZH08_03,Plate4,G4,Plate1,N8,.,1.867678351
Anderson_Mouse_BZH08_04,Plate4,H4,Plate1,P8,.,2.12046758
Anderson_Mouse_BZH08_05,Plate4,A5,Plate1,B10,.,2.232072607
Anderson_Mouse_BZH08_06,Plate4,B5,Plate1,D10,.,3.802077531
Anderson_Mouse_BZH08_07,Plate4,C5,Plate1,F10,.,2.555165382
Anderson_Mouse_BZH08_08,Plate4,D5,Plate1,H10,.,2.412521372
Anderson_Mouse_BZH08_09,Plate4,E5,Plate1,J10,.,3.473982132
Anderson_Mouse_BZH08_10,Plate4,F5,Plate1,L10,X,10
Anderson_ExtCon_P4G5,Plate4,G5,Plate1,N10,.,8.034445274
Anderson_ExtCon_P4H5,Plate4,H5,Plate1,P10,.,4.470390591
Singh_GF_61_wk2,Plate4,A6,Plate1,B12,.,4.272881601
Singh_GF_62_wk2,Plate4,B6,Plate1,D12,.,2.870889496
Singh_GF_63_wk2,Plate4,C6,Plate1,F12,.,2.727440589
Singh_GF_64_wk2,Plate4,D6,Plate1,H12,.,2.115264574
Singh_GF_65_wk2,Plate4,E6,Plate1,J12,.,4.177037904
Singh_GF_66_wk2,Plate4,F6,Plate1,L12,.,2.162470285
Singh_GF_67_wk2,Plate4,G6,Plate1,N12,.,2.709996989
Singh_GF_68_wk2,Plate4,H6,Plate1,P12,.,2.328266482
AviaunaInVitro_Plate_A1_BZH77_64,Plate4,A7,Plate1,B14,.,7.233058549
AviaunaInVitro_Plate_A2_BZH77_64,Plate4,B7,Plate1,D14,X,10
AviaunaInVitro_Plate_A3_BZH77_64,Plate4,C7,Plate1,F14,.,2.222794715
AviaunaInVitro_Plate_C1_BZH77_16,Plate4,D7,Plate1,H14,.,4.778650519
AviaunaInVitro_Plate_C2_BZH77_16,Plate4,E7,Plate1,J14,.,3.810190048
AviaunaInVitro_Plate_C3_BZH77_16,Plate4,F7,Plate1,L14,.,3.433192309
AviaunaInVitro_Plate_G1_BZH77_0,Plate4,G7,Plate1,N14,X,10
AviaunaInVitro_Plate_G2_BZH77_0,Plate4,H7,Plate1,P14,.,3.809609435
AviaunaInVitro_AB_A2_Blank,Plate4,A8,Plate1,B16,.,4.347748584
AviaunaInVitro_AB_BZH77_Fecal,Plate4,B8,Plate1,D16,.,3.840922805
AviaunaInVitro_Plate_G3_BZH77_0,Plate4,C8,Plate1,F16,.,3.084667015
AviaunaInVitro_Plate_A4_BZH64_64,Plate4,D8,Plate1,H16,.,5.778539775
AviaunaInVitro_Plate_A5_BZH64_64,Plate4,E8,Plate1,J16,.,2.015380985
AviaunaInVitro_Plate_A6_BZH64_64,Plate4,F8,Plate1,L16,.,6.068546662
AviaunaInVitro_Plate_C4_BZH64_16,Plate4,G8,Plate1,N16,.,1.814473365
AviaunaInVitro_Plate_C5_BZH64_16,Plate4,H8,Plate1,P16,.,2.423983278
AviaunaInVitro_Plate_C6_BZH64_16,Plate4,A9,Plate1,B18,.,3.716862775
AviaunaInVitro_Plate_G4_BZH64_0,Plate4,B9,Plate1,D18,.,3.576357559
AviaunaInVitro_Plate_G5_BZH64_0,Plate4,C9,Plate1,F18,.,2.667491099
AviaunaInVitro_Plate_G6_BZH64_0,Plate4,D9,Plate1,H18,X,10
AviaunaInVitro_Plate_A7_BZH42_64,Plate4,E9,Plate1,J18,.,4.954564169
AviaunaInVitro_Plate_A8_BZH42_64,Plate4,F9,Plate1,L18,.,9.87029446
AviaunaInVitro_Plate_A9_BZH42_64,Plate4,G9,Plate1,N18,.,1.837478348
AviaunaInVitro_Plate_C7_BZH42_16,Plate4,H9,Plate1,P18,.,2.302640138
AviaunaInVitro_Plate_C8_BZH42_16,Plate4,A10,Plate1,B20,.,3.202212344
AviaunaInVitro_Plate_C9_BZH42_16,Plate4,B10,Plate1,D20,.,2.677131753
AviaunaInVitro_Plate_G7_BZH42_0,Plate4,C10,Plate1,F20,.,3.126523203
AviaunaInVitro_Plate_G8_BZH42_0,Plate4,D10,Plate1,H20,.,2.59987349
AviaunaInVitro_Plate_G9_BZH42_0,Plate4,E10,Plate1,J20,.,1.725792013
AviaunaInVitro_Plate_A10_BZH08_64,Plate4,F10,Plate1,L20,.,2.390776766
AviaunaInVitro_AB_BZH64_Fecal,Plate4,G10,Plate1,N20,.,2.65157672
AviaunaInVitro_AB_H3_Blank,Plate4,H10,Plate1,P20,.,3.310665209
AviaunaInVitro_Plate_A11_BZH08_64,Plate4,A11,Plate1,B22,.,9.539790945
AviaunaInVitro_Plate_A12_BZH08_64,Plate4,B11,Plate1,D22,.,5.156922576
AviaunaInVitro_Plate_C10_BZH08_16,Plate4,C11,Plate1,F22,.,3.182644657
AviaunaInVitro_Plate_C11_BZH08_16,Plate4,D11,Plate1,H22,.,2.791392796
AviaunaInVitro_Plate_C12_BZH08_16,Plate4,E11,Plate1,J22,.,2.361140724
AviaunaInVitro_Plate_G10_BZH08_0,Plate4,F11,Plate1,L22,.,2.156780238
AviaunaInVitro_Plate_G11_BZH08_0,Plate4,G11,Plate1,N22,.,2.730344862
AviaunaInVitro_Plate_G12_BZH08_0,Plate4,H11,Plate1,P22,X,10
AviaunaInVitro_AB_BZH42_Fecal,Plate4,A12,Plate1,B24,.,2.727812586
AviaunaInVitro_AB_BZH08_Fecal,Plate4,B12,Plate1,D24,.,2.824746246
AviaunaInVitro_AB_C6_ExtCon1,Plate4,C12,Plate1,F24,.,3.322213883
AviaunaInVitro_AB_D6_ExtCon2,Plate4,D12,Plate1,H24,.,3.182239539
AviaunaInVitro_NTC1,Plate4,E12,Plate1,J24,.,5.840981612
AviaunaInVitro_NTC2,Plate4,F12,Plate1,L24,.,6.181841336
AviaunaInVitro_NTC3,Plate4,G12,Plate1,N24,.,4.037237867
AviaunaInVitro_NTC4,Plate4,H12,Plate1,P24,.,4.486435487
HKPInvitro_sFMT_PB_48_4,Plate5,A1,Plate2,A1,.,5.466748231
HKPInvitro_sFMT_HKP_2_4,Plate5,B1,Plate2,C1,.,6.13858092
HKPInvitro_sFMTd23_HKP_24_4,Plate5,C1,Plate2,E1,.,2.642747337
HKPInvitro_Positive_control,Plate5,D1,Plate2,G1,.,2.561776602
HKPInvitro_sFMTd23_HKP_48_4,Plate5,E1,Plate2,I1,.,2.080498221
HKPInvitro_sFMT_HKP_48_2,Plate5,F1,Plate2,K1,.,2.492310599
HKPInvitro_sFMTd23_HKP_48_2,Plate5,G1,Plate2,M1,.,3.290078669
HKPInvitro_sFMTd23_PB_4_1,Plate5,H1,Plate2,O1,.,5.683946432
HKPInvitro_sFMTd23_HKP_48_3,Plate5,A2,Plate2,A3,.,5.830764396
HKPInvitro_sFMT_HKP_0_1,Plate5,B2,Plate2,C3,X,10
HKPInvitro_sFMTd23_PB_0_1,Plate5,C2,Plate2,E3,X,10
HKPInvitro_sFMTd23_HKP_24_3,Plate5,D2,Plate2,G3,.,4.343405256
HKPInvitro_sFMT_PB_8_4,Plate5,E2,Plate2,I3,.,3.054982661
HKPInvitro_sFMT_HKP_48_1,Plate5,F2,Plate2,K3,.,6.559351306
HKPInvitro_sFMT_PB_24_2,Plate5,G2,Plate2,M3,X,10
HKPInvitro_sFMTd23_HKP_48_1,Plate5,H2,Plate2,O3,.,2.260887928
HKPInvitro_sFMTd23_PB_4_2,Plate5,A3,Plate2,A5,X,10
HKPInvitro_sFMT_HKP_48_3,Plate5,B3,Plate2,C5,.,3.726003143
HKPInvitro_sFMTd23_HKP_8_2,Plate5,C3,Plate2,E5,.,4.663654878
HKPInvitro_sFMT_PB_8_2,Plate5,D3,Plate2,G5,.,3.44324042
HKPInvitro_sFMT_HKP_8_3,Plate5,E3,Plate2,I5,.,2.051306877
HKPInvitro_sFMTd23_PB_2_1,Plate5,F3,Plate2,K5,.,3.404903265
HKPInvitro_sFMTd23_PB_2_3,Plate5,G3,Plate2,M5,.,3.828863582
HKPInvitro_sFMT_PB_24_3,Plate5,H3,Plate2,O5,.,3.007391266
HKPInvitro_sFMTd23_PB_2_2,Plate5,A4,Plate2,A7,X,10
HKPInvitro_sFMTd23_PB_4_3,Plate5,B4,Plate2,C7,.,5.220729848
HKPInvitro_sFMT_PB_8_3,Plate5,C4,Plate2,E7,.,2.154178428
HKPInvitro_sFMT_HKP_48_4,Plate5,D4,Plate2,G7,.,2.478228146
HKPInvitro_sFMT_HKP_4_2,Plate5,E4,Plate2,I7,.,2.628507053
HKPInvitro_sFMT_HKP_2_2,Plate5,F4,Plate2,K7,.,5.495891546
HKPInvitro_sFMT_HKP_4_4,Plate5,G4,Plate2,M7,.,2.226803995
HKPInvitro_sFMTd23_PB_24_1,Plate5,H4,Plate2,O7,.,2.286738222
HKPInvitro_sFMT_HKP_0_3,Plate5,A5,Plate2,A9,X,10
HKPInvitro_sFMTd23_PB_4_4,Plate5,B5,Plate2,C9,.,2.380362391
HKPInvitro_sFMTd23_PB_8_2,Plate5,C5,Plate2,E9,.,2.664009051
HKPInvitro_sFMT_HKP_8_4,Plate5,D5,Plate2,G9,X,10
HKPInvitro_sFMTd23_PB_24_3,Plate5,E5,Plate2,I9,.,4.40909137
HKPInvitro_sFMT_PB_4_2,Plate5,F5,Plate2,K9,.,4.11194186
HKPInvitro_sFMTd23_HKP_0_4,Plate5,G5,Plate2,M9,.,3.231079365
HKPInvitro_sFMT_HKP_8_2,Plate5,H5,Plate2,O9,.,3.90359525
HKPInvitro_sFMT_PB_2_2,Plate5,A6,Plate2,A11,.,3.991950631
HKPInvitro_sFMT_PB_2_4,Plate5,B6,Plate2,C11,X,10
HKPInvitro_sFMT_PB_48_1,Plate5,C6,Plate2,E11,.,2.993885587
HKPInvitro_sFMTd23_HKP_8_3,Plate5,D6,Plate2,G11,.,7.31079124
HKPInvitro_sFMT_PB_4_4,Plate5,E6,Plate2,I11,X,10
HKPInvitro_sFMT_HKP_0_4,Plate5,F6,Plate2,K11,.,6.907789984
HKPInvitro_sFMTd23_HKP_0_3,Plate5,G6,Plate2,M11,.,2.317904818
HKPInvitro_sFMTd23_PB_48_2,Plate5,H6,Plate2,O11,.,2.288674654
HKPInvitro_sFMTd23_PB_8_3,Plate5,A7,Plate2,A13,.,3.785669047
HKPInvitro_sFMTd23_HKP_2_4,Plate5,B7,Plate2,C13,.,6.738358307
HKPInvitro_sFMT_HKP_2_3,Plate5,C7,Plate2,E13,X,10
HKPInvitro_sFMTd23_PB_24_4,Plate5,D7,Plate2,G13,X,10
HKPInvitro_sFMTd23_HKP_4_2,Plate5,E7,Plate2,I13,.,4.276353348
HKPInvitro_sFMTd23_PB_0_4,Plate5,F7,Plate2,K13,.,4.255788191
HKPInvitro_sFMTd23_HKP_2_3,Plate5,G7,Plate2,M13,.,2.204128288
HKPInvitro_sFMTd23_HKP_8_1,Plate5,H7,Plate2,O13,.,3.008386479
HKPInvitro_sFMT_PB_48_2,Plate5,A8,Plate2,A15,.,3.636309422
HKPInvitro_sFMTd23_HKP_24_1,Plate5,B8,Plate2,C15,.,5.129149418
HKPInvitro_sFMT_PB_4_1,Plate5,C8,Plate2,E15,.,2.096549897
HKPInvitro_sFMT_HKP_24_2,Plate5,D8,Plate2,G15,X,10
HKPInvitro_sFMT_PB_48_3,Plate5,E8,Plate2,I15,.,1.933435303
HKPInvitro_sFMTd23_PB_24_2,Plate5,F8,Plate2,K15,.,1.899140088
HKPInvitro_Negative_control,Plate5,G8,Plate2,M15,.,3.378788171
HKPInvitro_sFMTd23_PB_2_4,Plate5,H8,Plate2,O15,X,10
HKPInvitro_sFMTd23_PB_8_4,Plate5,A9,Plate2,A17,.,3.627340133
HKPInvitro_sFMTd23_PB_0_3,Plate5,B9,Plate2,C17,.,2.787968577
HKPInvitro_sFMT_PB_0_2,Plate5,C9,Plate2,E17,X,10
HKPInvitro_sFMT_PB_24_4,Plate5,D9,Plate2,G17,X,10
HKPInvitro_sFMTd23_PB_48_1,Plate5,E9,Plate2,I17,.,4.316408265
HKPInvitro_sFMT_PB_2_3,Plate5,F9,Plate2,K17,X,10
HKPInvitro_sFMT_PB_24_1,Plate5,G9,Plate2,M17,.,3.000263123
HKPInvitro_sFMT_HKP_24_4,Plate5,H9,Plate2,O17,.,3.632874756
HKPInvitro_sFMTd23_PB_0_2,Plate5,A10,Plate2,A19,.,2.745863974
HKPInvitro_sFMT_HKP_4_1,Plate5,B10,Plate2,C19,.,2.479026813
HKPInvitro_sFMT_HKP_24_1,Plate5,C10,Plate2,E19,.,2.866938777
HKPInvitro_sFMTd23_PB_48_3,Plate5,D10,Plate2,G19,.,2.329948152
HKPInvitro_sFMT_PB_2_1,Plate5,E10,Plate2,I19,.,3.506138021
HKPInvitro_sFMTd23_HKP_24_2,Plate5,F10,Plate2,K19,.,1.681819581
HKPInvitro_sFMT_HKP_4_3,Plate5,G10,Plate2,M19,.,2.486176239
HKPInvitro_sFMTd23_HKP_4_4,Plate5,H10,Plate2,O19,.,2.68000164
HKPInvitro_sFMTd23_PB_48_4,Plate5,A11,Plate2,A21,.,4.316967279
HKPInvitro_sFMTd23_HKP_2_1,Plate5,B11,Plate2,C21,.,6.803456973
HKPInvitro_sFMT_PB_4_3,Plate5,C11,Plate2,E21,.,3.743438221
HKPInvitro_sFMTd23_PB_8_1,Plate5,D11,Plate2,G21,.,4.133869579
HKPInvitro_sFMT_PB_8_1,Plate5,E11,Plate2,I21,.,1.782295779
HKPInvitro_sFMTd23_HKP_8_4,Plate5,F11,Plate2,K21,X,10
HKPInvitro_sFMT_PB_0_3,Plate5,G11,Plate2,M21,.,5.564393667
HKPInvitro_sFMTd23_HKP_4_3,Plate5,H11,Plate2,O21,.,2.712937811
HKPInvitro_sFMTd23_HKP_4_1,Plate5,A12,Plate2,A23,.,2.975268674
HKPInvitro_sFMTd23_HKP_0_2,Plate5,B12,Plate2,C23,.,3.079442535
HKPInvitro_sFMT_HKP_2_1,Plate5,C12,Plate2,E23,.,3.672229973
HKPInvitro_sFMT_HKP_0_2,Plate5,D12,Plate2,G23,.,2.7630866
HKPInvitro_sFMT_PB_0_1,Plate5,E12,Plate2,I23,.,2.838376324
HKPInvitro_sFMTd23_HKP_2_2,Plate5,F12,Plate2,K23,.,3.238718491
HKPInvitro_sFMT_HKP_8_1,Plate5,G12,Plate2,M23,.,2.55758335
HKPInvitro_sFMT_HKP_24_3,Plate5,H12,Plate2,O23,.,4.960216583
Macalady1_1b,Plate6,A1,Plate2,B1,X,10
Macalady1_1b2b,Plate6,B1,Plate2,D1,X,10
Macalady1_1b2c,Plate6,C1,Plate2,F1,X,10
Macalady1_1b2b3a,Plate6,D1,Plate2,H1,X,10
Macalady1_1b2c3a,Plate6,E1,Plate2,J1,X,10
Macalady1_1a,Plate6,F1,Plate2,L1,X,10
Macalady1_1a2b,Plate6,G1,Plate2,N1,X,10
Macalady1_1a2c,Plate6,H1,Plate2,P1,X,10
Macalady1_1a2b3b,Plate6,A2,Plate2,B3,.,6.029032202
Macalady1_1a2c3a,Plate6,B2,Plate2,D3,.,2.92745103
Macalady1_1b2c3a4a,Plate6,C2,Plate2,F3,.,6.699983451
Macalady1_ExtCon_LV,Plate6,D2,Plate2,H3,.,5.986801497
Macalady1_ExtCon_DHS,Plate6,E2,Plate2,J3,.,2.857109388
Macalady1_DHS1,Plate6,F2,Plate2,L3,.,6.592214199
Macalady1_DHS2,Plate6,G2,Plate2,N3,.,3.593579137
Macalady1_NTC1,Plate6,H2,Plate2,P3,.,3.204675237
Empty_Plate6_A3,Plate6,A3,Plate2,B5,.,3.047627407
Empty_Plate6_B3,Plate6,B3,Plate2,D5,.,4.814541456
Empty_Plate6_C3,Plate6,C3,Plate2,F5,.,2.853359303
Empty_Plate6_D3,Plate6,D3,Plate2,H5,X,10
Empty_Plate6_E3,Plate6,E3,Plate2,J5,.,2.93096894
Empty_Plate6_F3,Plate6,F3,Plate2,L5,.,2.794200692
Empty_Plate6_G3,Plate6,G3,Plate2,N5,X,10
Empty_Plate6_H3,Plate6,H3,Plate2,P5,.,3.995778859
'''

# Tweakable parameters
ChangeTip = True #should tips be changed between samples? 
ChangeFrequency = 8 # how frequently should tips be changed if ChangeTip = true. 1 = every sample, 8 = every column.
newtube_volume = 1200 # pause protocol when tube gets to this volume in ul

#Don't edit below this line unless you want to change the functionality of the script
loadings_parsed = loadings.splitlines()[1:] # Discard the blank first line.
whichplates = [row["plate384"] for row in csv.DictReader(loadings_parsed)]
whichplates = numpy.unique(whichplates)

def run(protocol: protocol_api.ProtocolContext):

    # define labware, only load the plates that are specified in the csv file
    if 'Plate1' in whichplates: Plate1 = protocol.load_labware('biorad_384_wellplate_50ul', '1')
    if 'Plate2' in whichplates: Plate2 = protocol.load_labware('biorad_384_wellplate_50ul', '2')


    epitube = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '7') # eppendorf microcentrifuge tube in rack on position 3
    tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10') # 20ul filter tips on deck position 1

    # define pipettes
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips])

	#loop through every line in the csv to be transferred
    left_pipette.pick_up_tip()
    i=0 # a counter to know when to change tips
    total_volume = 0 # tracking the total volume in the tube
    for transfer in csv.DictReader(loadings_parsed):
        check = i % ChangeFrequency #checking the remainder to know when to change tips
        if ChangeTip and check == 0 and i != 0:
            left_pipette.drop_tip()
            left_pipette.pick_up_tip()
        left_pipette.aspirate(float(transfer['volume']), eval(transfer['plate384'])[transfer['well384']])
        left_pipette.dispense(float(transfer['volume']), epitube['A1'])
        i=i+1
        total_volume = total_volume + float(transfer['volume'])
        if total_volume > newtube_volume:
            protocol.home()	
            protocol.comment("Total volume is currently" + str(total_volume) + " ul")
            protocol.pause("Please insert new 1.5mL eppendorf tube")
            total_volume = 0
    protocol.comment("Total volume in tube is " + str(total_volume) + " ul")
    left_pipette.drop_tip()
