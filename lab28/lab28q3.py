"""A DNA fragment of unknown orientation:
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
1. Translate all six reading frames: frames +1, +2 and +3 start at positions 0, 1 and 2
of mystery; frames -1, -2 and -3 do the same on its reverse complement.
2. Find the longest open reading frame: a stretch that starts with M and ends at a stop
codon.
Hint: trim each frame to a multiple of 3 bases before translating (s[:len(s) - len(s) % 3]),
otherwise Biopython warns about a partial codon."""

import re
from Bio.Seq import Seq
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
rev= mystery.reverse_complement()

proteins=[]
for strand,sequence in [("+",mystery),("-",rev)]:
    for frame in range(3):
        s=sequence[frame:]
        s=s[:len(s)-len(s)%3]
        protein=str(s.translate())
        print(f"Frame {strand}{frame+1} : {protein}")
        orfs=re.findall(r"M[A-Z]*\*",protein)
        for orf in orfs:
            proteins.append((len(orf),str(strand)+str(frame+1),orf))

longest_orf=max(proteins, key=lambda x:x[0])
print("Longest ORF :",longest_orf[2])
print("Length :",longest_orf[0])
print('Reading Frame',longest_orf[1])
