#!/usr/bin/python3
import sys
import string
# run as: python3 parse_cluster_table.py Osat CLUSTER_TABLE.class

clust_tabs = sys.argv[1:]

# Annotation list:
annot_list = ["All", "All/organelle", "All/organelle/mitochondria", "All/organelle/plastid", "All/repeat", "All/repeat/mobile_element", "All/repeat/mobile_element/Class_II/Subclass_1/TIR/EnSpm_CACTA", "All/repeat/mobile_element/Class_II/Subclass_1/TIR/hAT", "All/repeat/mobile_element/Class_II/Subclass_1/TIR/MuDR_Mutator", "All/repeat/mobile_element/Class_II/Subclass_1/TIR/Tc1_Mariner", "All/repeat/mobile_element/Class_II/Subclass_2/Helitron", "All/repeat/mobile_element/Class_I/LINE", "All/repeat/mobile_element/Class_I/LTR", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Ale", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Alesia", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Angela", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Bianca", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Ikeros", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Ivana", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/SIRE", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/TAR", "All/repeat/mobile_element/Class_I/LTR/Ty1_copia/Tork", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/chromovirus/CRM", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/chromovirus/Galadriel", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/chromovirus/Reina", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/chromovirus/Tekay", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/non-chromovirus/OTA/Athila", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/non-chromovirus/OTA/Tat", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/non-chromovirus/OTA/Tat/Ogre", "All/repeat/mobile_element/Class_I/LTR/Ty3_gypsy/non-chromovirus/OTA/Tat/Retand", "All/repeat/mobile_element/Class_I/pararetrovirus", "All/repeat/rDNA/45S_rDNA", "All/repeat/rDNA/45S_rDNA/18S_rDNA", "All/repeat/rDNA/45S_rDNA/25S_rDNA", "All/repeat/rDNA/5S_rDNA", "All/repeat/satellite"]
spec_holomono_dict = {"Cacu":'holocentric', "Chlut":'holocentric', "Cpap":'holocentric', 
"Dcap":'holocentric', "Dfil":'holocentric', "Dlus":'monocentric', 
"Euni":'holocentric', "Lele":'holocentric', "Lpil":'holocentric', 
"Nven":'monocentric', "Osat":'monocentric', "Pqua":'monocentric', 
"Race":'monocentric', "Ralp":'monocentric', "Scer":'monocentric'}

def fill_dict(clust_tabs):
    in_dict = {}
    for csv in clust_tabs:
        spec = csv.split("_")[0]
        in_dict[spec] = {}
        with open (csv) as tab:
            for l in tab:
                line_list = l.rstrip().replace("\"","").split("\t")
                if "Number_of" in line_list[0]:
                    in_dict[spec][line_list[0]] = line_list[1]
                if str(line_list[0]).isdigit():
                    sup_clstr = line_list[1]
                    size = line_list[2]
                    aut_annot = line_list[4]
                    if sup_clstr not in in_dict[spec].keys():
                        in_dict[spec][sup_clstr] = {}
                        if aut_annot not in in_dict[spec][sup_clstr].keys():
                            in_dict[spec][sup_clstr][aut_annot] = []
                            in_dict[spec][sup_clstr][aut_annot].append(int(size))
                        else:
                            in_dict[spec][sup_clstr][aut_annot].append(int(size))
                    else:
                        if aut_annot not in in_dict[spec][sup_clstr].keys():
                            in_dict[spec][sup_clstr][aut_annot] = []
                            in_dict[spec][sup_clstr][aut_annot].append(int(size))
                        else:
                            in_dict[spec][sup_clstr][aut_annot].append(int(size))
    return in_dict
in_dict = fill_dict(clust_tabs)

def gen_out_tsv(in_dict):
    out_name= "holoMono_RepExp_all_spec_prop.tsv"
    with open(out_name, 'w') as out:
        for s in in_dict.keys():
            tot_reads_cnt = int(in_dict[s]['Number_of_analyzed_reads'])
            for an in annot_list:
                an_read_cnts = 0
                for sc in in_dict[s].keys():
                    if sc.isdigit():
                        if an in in_dict[s][sc].keys():
                            an_read_cnts += sum(in_dict[s][sc][an])
                out.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(s, spec_holomono_dict[s], 
                an.replace("/","|"), "|".join(an.split("/")[-2:]), str(an_read_cnts), 
                str(tot_reads_cnt), 
                str(round((an_read_cnts/tot_reads_cnt)*100, 2))))

gen_out_tsv(in_dict)