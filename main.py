import re
def readMass(filename):
    file = open(filename,encoding="utf-8-sig")
    mass=[]
    N=0
    for row in file:
        z=[]
        rowStr = row.strip('\n')
        rowStr = row.strip(' ')
        rowStr = re.split(' +', rowStr)
        for i in rowStr:
            z.append(int(i))
        mass.append(z)
        N+=1
    return mass, N
mass,n=readMass(r'input.txt')
massofsummm=[]
i=0
while i <len(mass):
    j=0
    if i ==0:
        massofsummm=mass[i]
    else:
        while j<len(mass[i]):
            massofsummm[j] += mass[i][j]
            j+=1
    i+=1
i=0
z=1
max=massofsummm[0]
while i <len(massofsummm):
    print("%-3s"%massofsummm[i], end = " ")
    if massofsummm[i]>max:
        max=massofsummm[i]
        z=i+1
    i+=1
print("\n", z)
