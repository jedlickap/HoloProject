t <- read.table('holoMono_RepExp_all_spec_prop.tsv', sep = '\t', header=F)
headers <- c('spec','centromere','overall_annot','annotation','annot_reads','reads_total', 'repeat_prop')
colnames(t) <- headers
spec_order <- c("Lpil", "Lele", "Cacu", "Cpap","Euni","Dcap","Dfil","Chlut","Osat", "Scer", "Nven", "Dlus", "Race", "Ralp", "Pqua")
t$spec <- factor(t$spec, levels = spec_order)
a <- c(rep("#00688B",8), rep("#FF6103",7))

plot_generator <- function(data, title) {
  a <- c(rep("#00688B",8), rep("#FF6103",7))
  library('ggplot2')
  ggplot(data, aes(fill = annotation, x = spec, y = repeat_prop)) + 
    geom_bar(position="stack", stat="identity") +
    theme_bw() +
    theme(plot.title = element_text(size = 20, face = "bold"),
          axis.text.x = element_text(angle = 90, 
                                     vjust = 0.5, 
                                     hjust=1, 
                                     color = a),
          axis.text=element_text(size=12),
          axis.title=element_text(size=14,face="bold")) +
    scale_x_discrete(labels = c("Lpil"="Luzula pilosa", 
                                "Lele"="Luzula elegans", 
                                "Cacu"="Carex acutiformmis",
                                "Cpap"="Cyperus papyrus",
                                "Euni"="Eleocharis uniglumis",
                                "Dcap"="Drosera capensis",
                                "Dfil"="Drosera filiformis",
                                "Chlut"="Chamaelirium luteum",
                                "Osat"="Oryza sativa", 
                                "Scer"="Secale cereale", 
                                "Nven"="Nepenthes ventricosa", 
                                "Dlus"="Drosophyllum lusitanicum",
                                "Race"="Rumex acetosa", 
                                "Ralp"="Rumex alpinus", 
                                "Pqua"="Paris quadrifolia")) +
    ggtitle(title) +
    xlab("Plant species") +
    ylab("Repeats proportion [%]") +
    scale_fill_discrete(name = "Repeat type")
}

t_noAll <- subset(t, t$overall_annot != "All")
plot_generator(t_noAll, "RepeatExplorer - all annotated repeats")

t_all <- subset(t, t$overall_annot == "All")
plot_generator(t_all, "RepeatExplorer - unidentified repeats")

t_class_I <- t[grepl('Class_I[|]{1}', t$overall_annot),]
plot_generator(t_class_I, "RepeatExplorer - Class I")

t_class_II <- t[grepl('Class_II[|]{1}', t$overall_annot),]
plot_generator(t_class_II, "RepeatExplorer - Class II")

t_rDNA_sat <- t[grepl('rDNA|satellite', t$overall_annot),]
plot_generator(t_rDNA_sat, "RepeatExplorer - rDNA and satellites")

t_organelle <- (t[grepl('organelle', t$overall_annot),])
plot_generator(t_organelle, "RepeatExplorer - organelles")

pdf("class_I.pdf",width=15, height = 10)
ggplot(t_class_I, aes(fill = annotation, x = spec, y = repeat_prop)) + 
  geom_bar(position="stack", stat="identity") +
  theme_bw() +
  theme(# legend.position = 'bottom', 
    axis.text.x = element_text(angle = 90, 
                               vjust = 0.5, 
                               hjust=1, 
                               color = a)) +
  ggtitle("RepeatExplorer - Class I")
dev.off()

pdf("class_II.pdf",width=15, height = 10)
ggplot(t_class_II, aes(fill = annotation, x = spec, y = repeat_prop)) + 
  geom_bar(position="stack", stat="identity") +
  theme_bw() +
  theme(# legend.position = 'bottom', 
    axis.text.x = element_text(angle = 90, 
                               vjust = 0.5, 
                               hjust=1, 
                               color = a)) +
  ggtitle("RepeatExplorer - Class II")
dev.off()

pdf("organelles.pdf",width=15, height = 10)
ggplot(t_organelle, aes(fill = annotation, x = spec, y = repeat_prop)) + 
  geom_bar(position="stack", stat="identity") +
  theme_bw() +
  theme(# legend.position = 'bottom', 
    axis.text.x = element_text(angle = 90, 
                               vjust = 0.5, 
                               hjust=1, 
                               color = a)) +
  ggtitle("RepeatExplorer - Organelles")
dev.off()

pdf("rDNA_sats.pdf",width=15, height = 10)
ggplot(t_rDNA_sat, aes(fill = annotation, x = spec, y = repeat_prop)) + 
  geom_bar(position="stack", stat="identity") +
  theme_bw() +
  theme(# legend.position = 'bottom', 
    axis.text.x = element_text(angle = 90, 
                               vjust = 0.5, 
                               hjust=1, 
                               color = a)) +
  ggtitle("RepeatExplorer - rDNA and satellites")
dev.off()