"""to define a function analyse_dna with inner function gc_content """
def analyse_dna(d):
    def gc_content(at,gc):
        percent_gc=(gc/(at+gc))*100
        return percent_gc

    a = (d.lower()).count("a")
    t = (d.lower()).count("t")
    g = (d.lower()).count("g")
    c = (d.lower()).count("c")
    total_at=a+t
    total_gc=g+c
    if gc_content(total_at,total_gc)>50:
        print("The sequence is GC rich")
        print("GC% = "+str(gc_content(total_at,total_gc)))
    else :
        print("The sequence is AT rich")
        print("GC% = " + str(gc_content(total_at, total_gc)))

seq=input("Enter the DNA sequence: ")
analyse_dna(seq)

