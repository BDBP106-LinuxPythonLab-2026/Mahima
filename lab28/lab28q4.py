"""A cloning construct (49 bp) contains a BamHI site, a short coding sequence and an
EcoRI site:
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
1. Create a SeqRecord with id and name PLAB001, set annotations[”molecule type”] =
”DNA”, and add three features: a misc feature for the BamHI site at 0-6, a CDS at 8-41
with qualifiers gene = labA and translation = MASKGEELFT, and a misc feature for
the EcoRI site at 41-47 (Python-style positions).
2. Write it to lab construct.gb in GenBank format; open the file in a text editor and
find the FEATURES table.
3. Read it back with SeqIO.read() and list every feature with its type, its 1-based start
and end, and its gene or note.
4. Extract the CDS, translate it, and check that the result matches the stored translation
qualifier."""
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature ,SimpleLocation
from Bio import SeqIO
#1
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
record=SeqRecord( Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC"),id="PLAB001",name="PLAB001",description="Creating a record for lab 28 of python class.")
record.annotations["molecule_type"]="DNA"
record.annotations["date"]="07-NOV-2026"
BamHI= SeqFeature(SimpleLocation(0,6),type="misc",qualifiers={"note":'BamHI site'})
record.features.append(BamHI)
cds=SeqFeature(SimpleLocation(8,41),type="CDS",qualifiers={"note":"LabA","Translation":"MASKGEELFT"})
record.features.append(cds)
EcoRI=SeqFeature(SimpleLocation(41,47),type="misc",qualifiers={"note":"EcoRI site"})
record.features.append(EcoRI)
#print(record)

#2
SeqIO.write(record,"lab_construct.gb","genbank")

#3

gb=SeqIO.read('lab_construct.gb',"genbank")
for feature in gb.features:
    print(feature.type,feature.location,feature.qualifiers['note'][0])



#4

cds=gb.features[1].extract(gb.seq)
print(cds,cds.translate())
print("Stored translation qualifier same as translation:",cds.translate()=="MASKGEELFT*")