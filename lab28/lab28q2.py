import Bio
from Bio.Seq  import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature ,SimpleLocation
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO

# (2) Do the following.
# 1. Read lab genes.fasta with SeqIO.parse() into a list and print how many records it has.
# 2. Print a table of ID, length, GC % (1 decimal place) and the protein translated up to
# the first stop codon.
# 3. Write the genes with GC content of at least 50% to lab high gc.fasta, and print how
# many were written.
# 4. Print the IDs sorted from highest to lowest GC content, using sorted() with a lambda.

#1
records=list(SeqIO.parse("lab_genes.fasta","fasta"))
print("Number of records:",len(records))

#2
print("ID","Length","GC%","Protein")
for i in range(len(records)):
    print(records[i].id,len(records[i].seq),round(gc_fraction(records[i].seq)*100,1),records[i].seq.translate(to_stop=True))

#3
high_gc=[r for r in records if gc_fraction(r.seq)>=0.5]
count=SeqIO.write(high_gc,"lab_high_gc.fasta","fasta")
print(count,"records written to lab_high_gc.fasta")

#4
sorted_records = sorted(
    records,
    key=lambda record: gc_fraction(record.seq),
    reverse=True
)

print("\nIDs sorted by GC content (highest to lowest):")

for record in sorted_records:
    print(record.id)