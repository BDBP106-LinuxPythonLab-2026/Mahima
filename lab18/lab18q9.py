def codon_extracter(seq):
    print(seq)
    codons=[]
    a=int(input("From which codon do you want the reading frame to start : "))
    for i in range(-1+a,len(seq),3):
        if i+2<len(seq):
            codons.append(seq[i]+seq[i+1]+seq[i+2])
    return codons

test=codon_extracter("GTTTCGATTATAACG")
print(test)