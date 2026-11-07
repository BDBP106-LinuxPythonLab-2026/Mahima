import Bio
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

thrL= Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print(len(thrL))
print(round(gc_fraction(thrL)*100,2))
print(thrL.translate())
print(thrL.translate(to_stop=True))
print(thrL.count("ACC"))
print(thrL[-1])
print(thrL.reverse_complement()[:13])