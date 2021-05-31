library(DiagrammeR)

grViz("
digraph dot {

 graph [layout = dot]

 node [shape = box,
 style = filled,
 color = black,
 label = '']

 # node [fillcolor = white,fixedsize = true, width = 2]
 node [fillcolor = white]
 a[label = 'minion_pass_reads.fastq.gz']

 node [fillcolor = white]
 b[label = 'NanoFilt \n l_500, q >= 7, headCrop = 75'] 
 c[label = 'canu \n -correct'] 
 d[label = 'assembly']

 node [fillcolor = white]

 edge [color = black]
 a -> b -> c -> d
 d -> {e[label = 'canu \n -assemble';color=blue] f[label = 'flye';color=green]}
 }")