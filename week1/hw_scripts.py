"""1. query.tsv --> 1000_homologs.fa"""

awk '{gsub ("-","")}{print ">" $1 "\n" $2}' blast_alignment.tsv > 1000_logs.fa

"""2. 1000_homologs.fa --> 1000_h_proteins.fa"""

transeq 1000_logs.fa 1000_homo_pt.fa

"""3. 1000_h_proteins.fa --> alignment_prot.fa"""

mafft 1000_homo_pt.fa > alignpt.fa