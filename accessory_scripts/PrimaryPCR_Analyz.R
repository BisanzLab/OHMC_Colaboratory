##########################
message("#################################################################################################################")
message("#PrimaryPCR Analyzer v0.11")
message("#J Bisanz 30 July 2024")
message("#Visualizes qPCR results from primary PCR for both cfx384 and qiaquant instruments")
message("#################################################################################################################")
message(" ")

theme_plt<-function () {
  theme_classic(base_size = 8, base_family = "Helvetica") + 
    theme(panel.border = element_rect(color = "black", linewidth = 1, 
                                      fill = NA)) + theme(axis.line = element_blank(), 
                                                          strip.background = element_blank())
}

#.libPaths("/data/shared_resources/Rlibs_4.1.0")

##########################
#Get arguments
suppressMessages(library(optparse))
option_list = list(
  make_option(c("-c", "--csv"), type="character", help="The output file containing quantification information, ex Quantification Amplification Results_SYBR.csv for cfx384", metavar="character"),
  make_option(c("-t", "--tracking"), type="character", help="The indexing tracking sheet (an excel file downloaded from AmpliconSeq).", metavar="character"),
  make_option(c("-i", "--plateid"), type="numeric", default="1", help="Which plates were analyzed (to pull names from) use the 384 well plate numbers. IE 1 is 1-4 and 2 is 5-6", metavar="character"),
  make_option(c("-u", "--instrument"), type="character", default="cfx384", help="Which instrument is data from? Use cfx384 or qiaquant384 as options.", metavar="numeric"),
  make_option(c("-p", "--pdf"), type="character", default="PrimaryCurves_96Plate[0-9].tsv", help="the output name for the per 96-well plates of the amplification_curves.", metavar="character"),
  make_option(c("-o", "--tsv"), type="character", default="PrimaryCurves_384Plate[0-9].tsv", help="the output name for the raw amplification data.", metavar="character"),
  make_option(c("-l", "--libpath"), type="character", default="/data/shared_resources/Rlibs_4.3.3", help="Location", metavar="numeric")
)

opt_parser = OptionParser(option_list=option_list)
opt = parse_args(opt_parser)

.libPaths(opt$libpath)


#opt$csv="libraryprep/BSUPLATE1_July162024.csv"
#opt$instrument="qiaquant384"
#opt$tracking="libraryprep_v2/NextSeq3_Tracking_2023July30.xlsx"
#opt$plateid="1"

###########
if (is.null(opt$csv) | is.null(opt$tracking) | is.null(opt$plateid)){
  print_help(opt_parser)
  stop("Specify the ampification results (--csv), tracking sheet (--tracking), instrument (--instrument), and plate ID (--plateid)")
}

message(date(), "---> Loading tidyverse and readxl")
suppressMessages(library(tidyverse))
suppressMessages(library(readxl))


###########
message(date(), paste("---> Reading ", opt$tracking, "and extracting 384 well plate", opt$plateid ))
tracking<-read_excel(opt$tracking, "SampleSheet.csv", skip=19)
if(length(tracking$Sample_ID)!=length(unique(tracking$Sample_ID))){
  tracking %>% filter(duplicated(Sample_ID)) %>% arrange(Sample_ID) %>% print()
  stop("There are duplicated sample names, please make sure every sample has a unique name!")
  }

suppressMessages(
  layout384<-
  bind_rows(
  read_excel(opt$tracking, "384_layout", n_max=16) %>% dplyr::rename(Col384=1) %>% pivot_longer(!Col384, names_to = "Row384", values_to = "Sample_ID") %>% mutate(Plate384="Plate384_1"),
  read_excel(opt$tracking, "384_layout", n_max=16, skip=18) %>% dplyr::rename(Col384=1) %>% pivot_longer(!Col384, names_to = "Row384", values_to = "Sample_ID") %>% mutate(Plate384="Plate384_2")
  ) %>%
    filter(!is.na(Sample_ID))
)

suppressMessages(
  tracking<-
  tracking %>%
    left_join(layout384) %>%
    filter(Plate384==paste0("Plate384_", opt$plate)) %>%
    mutate(Well384=paste0(Col384,Row384))
)
rm(layout384)

#write_tsv(tracking, paste0("Tracking_96_to_384_Plate",opt$plateid,".tsv"))
###########
message(date(), paste("---> Reading ", opt$csv, "for instrument", opt$instrument ))

if(opt$instrument=="cfx384"){
  suppressMessages(suppressWarnings(amps<-read_csv(opt$csv)))
  amps<-
    amps %>%
    select(-1) %>%
    gather(-Cycle, key="Well384", value="RFU")
} else if(opt$instrument=="qiaquant384"){
  suppressMessages(suppressWarnings(amps<-read_csv(opt$csv, skip=21)))
  amps<-
    amps %>%
    rename(Well384=1) %>%
    gather(-Well384, key="Cycle", value="RFU") %>%
    mutate(Cycle=as.numeric(Cycle))
} else {
  stop("Instrument must be either cfx384 or qiaquant384")
}

suppressMessages(
amps<-
amps %>% left_join(tracking %>% dplyr::select(Well384, Sample_Plate, Sample_Well, Sample_ID)) %>%
  mutate(Col96=gsub("[A-z]","", Sample_Well) %>% as.numeric()) %>%
  mutate(Row96=gsub("[0-9]","", Sample_Well)) %>%
  filter(!is.na(Sample_ID)) %>%
  mutate(SampleType=case_when(
    grepl("ZymoCom_|ZymoDNA|myco", Sample_ID) ~ "Positive Control",
    grepl("NTC_|ExtCon_", Sample_ID) ~ "Negative Control",
    TRUE ~ "Unknown"
  ))
)

###########
message(date(), paste("---> Plotting ", opt$csv, "for instrument", opt$instrument ))

for(i in unique(amps$Sample_Plate)){
  if(grepl("PrimaryCurves_96Plate", opt$pdf)){pdfname<-paste0("PrimaryCurves_96",i,".pdf")} else {pdfname<-paste0(opt$pdf,i,".pdf")}
  amps %>%
    filter(Sample_Plate==i) %>%
    ggplot(aes(x=Cycle, y=RFU, color=SampleType)) +
    geom_line() +
    facet_grid(Row96~Col96) +
    theme_plt() +
    geom_text(aes(label=paste0("\n", gsub("(.{12})(?=.)", "\\1\n", Sample_ID, perl=TRUE)), x=1, y=Inf), color="black", size=2, hjust=0, vjust=1.2, lineheight=0.8) +
    scale_color_manual(values=c("indianred","green", "grey50")) +
    ggtitle(paste("Primary PCR Curves 96:", i))
    
  ggsave(pdfname, height=7.5, width=10, useDingbats=F)
}

