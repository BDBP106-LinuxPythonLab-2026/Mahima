txt_mat=""
for i in range(65,77,4):
    txt_mat+=((chr(i))+" "+(chr(i+1))+" "+(chr(i+2))+" "+(chr(i+3))+"\n")

fout=open("stringmatrix.dat","wt")
bytes_written=fout.write(txt_mat)
print(bytes_written)
fout.close()
