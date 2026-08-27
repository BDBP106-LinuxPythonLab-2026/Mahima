#Question4
awk '$6=="PHE" { print $0}' 1HK0.cif > PHE_atoms.xyz
