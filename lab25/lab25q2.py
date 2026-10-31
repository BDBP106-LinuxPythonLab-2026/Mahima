def timer(func):
    import time
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Execution time: {end-start:.6f} seconds")
        return result
    return wrapper



class LinearAlgebra:
    def __init__(self,m1,m2):
        self._m1=m1
        self._m2=m2
       #validate matrices during initialization
        self.validate_matrices(m1,m2)

    @staticmethod
    def validate_matrices(m1,m2):
        # check that both matrices are non-empty
        if not m1 or not m2:
            raise ValueError("Matrices cannot be empty.")

        #check that all rows have the same number of columns
        if any(len(row) != len(m1[0]) for row in m1):
            raise ValueError("Matrix 1 has inconsistent row lengths.")
        if any(len(row) != len(m2[0]) for row in m2):
            raise ValueError("Matrix 2 has inconsistent row lengths.")

        #Check the matrix multiplication condition
        if len(m1[0]) != len(m2):
            raise ValueError("Matrix multiplication is not possible: columns of M1 must equal rows of M2")

    @property
    def m1(self):   #getter
        return self._m1

    @m1.setter
    def m1(self,new_m1):
        self._m1=new_m1

    @property
    def m2(self):
        return self._m2
    @m2.setter
    def m2(self,new_m2):
        self._m2=new_m2


    @timer
    def multiply(self):
        m3=[]
        for i in range(0,len(self.m1)):
            row=[]
            for k in range(0,len(self.m2)):
                a=0
                for j in range(len(self.m1[i])):
                    a+=self.m1[i][j] * self.m2[j][k]
                row.append(a)
            m3.append(row)

        return m3






m1=[[i for i in range(50) ] for _ in range(50)]
m2=[[i for i in range(50)] for _ in range(50)]

matrix=LinearAlgebra(m1,m2)
print(matrix.multiply())