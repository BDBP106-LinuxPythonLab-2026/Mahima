def protien_energy(temp):
    def calculate_free_energy(h,s,t):
        g=h-(t*s)
        return g
    enthalpy=float(input("Enthalpy: "))
    entropy=float(input("Entropy:"))
    G=calculate_free_energy(enthalpy,entropy,temp)
    if G<0:
        return "stable"
    else:
        return "nonstable"

p1=protien_energy(25)
print(p1)