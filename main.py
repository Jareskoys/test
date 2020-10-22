import re
import re
def readMass(filename):
    with open(filename) as file:
        file=open(filename)
        mass=[]
        N=0
        for row in file:
            z=[]
            rowStr=row.strip('\n')
            rowStr=re.split(" +", rowStr)
            print(rowStr)
            for i in rowStr:
                z.append(int(i))
            mass.append(z)
            N+=1
    return mass, N
def printMass(mass,N):
    for i in range(N):
        for j in range(N):
            print("%-4d"% mass[i][j],end='')
def ecxchange(mass, N):
    for i in range(N):
        for j in range(N):
            if i==j:
                mass[i][j],mass[i][N-1-i]=mass[i][N-1-i],mass[i][j]
    return mass


