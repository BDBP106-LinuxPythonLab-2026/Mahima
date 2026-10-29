fin=open("stringmatrix.dat","rt")
lines=fin.readlines()
fin.close()


grid=[]
for line in lines:
    a=line.replace("\n","")
    b=a.split()
    grid.append(b)

print(grid)

columns=len(grid[0])
rows=len(grid)
#print(rows,columns)

columns_as_list=[]
for i in range(0,columns):
    a=[]
    for j in range(0,rows):
        a.append(grid[j][i])
    columns_as_list.append(a)
print(columns_as_list)

diagonals=[]

for d in range(rows + columns -1):
    diagonal=[]
    for i in range(rows):
        j=d-i
        if 0  <= j < columns:
            diagonal.append(grid[i][j])
    if diagonal :
        diagonals.append(diagonal)

print(diagonals)

