def log_function_call(func):
    def wrapper(*args,**kwargs):
        print("Running DNA analysis.....")
        func(*args,**kwargs)
        print("Analysis complete!")
    return wrapper



@log_function_call
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

