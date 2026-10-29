def dot(v1,v2):
    product=0
    for i in range(len(v1)):
        product+=v1[i]*v2[i]
    return product

def matrix_vector(m,v):
    res_v=[0 for i in v]

    for component in res_v:
        row=0
        for j in range(len(m)):
            row+=m[0][j]*v[j]
        res_v[component]=row

    return res_v


def matrix_matrix(m1,m2):
    m3=[]
    for i in range(0,len(m1)):
        row=[]
        for k in range(0,len(m2)):
            a=0
            for j in range(0,len(m1[i])):
                a+=m1[i][j]*m2[j][k]
            row.append(a)
        m3.append(row)

    return m3
def cross(v1,v2):
    v3=[]
    for i in range(len(v1)):
        x=(i+1)%3
        y=(i+2)%3
        v3.append(v1[x]*v2[y]-v1[y]*v2[x])
    return v3

#print(matrix_vector([[1,2],[3,4]],[5,6]))
#print(matrix_matrix([[1,2],[3,4]],[[2,3],[3,4]]))


