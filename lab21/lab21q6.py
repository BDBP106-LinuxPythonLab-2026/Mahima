"""Write a function cell_metabolism with an inner function energy_output"""

def cell_metabolism(g,o):
    def energy_output(x):
        return x*38
    if g==o/6:
        atp=energy_output(g)
    elif g>o/6:
        atp=energy_output(o//6)
    elif g<0/6:
        atp=energy_output(g)
    return atp


#atp1=cell_metabolism(2,12)
#atp2=cell_metabolism(2,8)
#atp3=cell_metabolism(3,16)
#print(atp1,atp2,atp3) #to check if the func is working