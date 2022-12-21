import numpy as np 
s=int(input("ENTER WHICH SQUARE MATRIX YOU WANT: "))
data=""
for H in range(s):
    G=input("ENTER VALUE FOR {} ROW OF MATRIX(SEPARATED BY SPACES): ".format(H+1))
    data+=G
    if H!=s-1:
        data+=";"
    print()
mat=np.matrix(data)  
print(mat)
TRANS=mat.T
print("TRANSPOSE OF MATRIX: \n",TRANS)