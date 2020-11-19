"""
ID: ca6fqb1
LANG: PYTHON2
TASK: wormhole
"""
fin = open("wormhole.txt","r")
num = int(fin.readline().strip())
coor = [list(map(int,fin.readline().strip().split(" "))) for i in range(num)]
X= [coor[i][0] for i in range(num)]
X = [0]+X
Y= [coor[i][1] for i in range(num)]
Y=[0]+Y
print(X,Y)
partner = [0 for k in range(num+1)]
nextright = [0 for i in range(num+1)]
for i in range(1,num+1):
    for j in range(1,num+1):
        if X[j]>X[i]:
            if nextright[i]==0 or X[j]-X[i]<X[nextright[i]]-X[i]:
                nextright[i]=j
def cicle():
    for start in range(1,num+1):
        pos = start
        for count in range(num):
            pos = nextright[partner[pos]]
        if pos!=0:
            return True
    return False
def solve():
    i,total=0,0
    for i in range(1,num+1):
        if partner[i]==0:
            break
    if i==num:
        if cicle():
            return True
        return False
    for j in range(i+1,num+1):
        if partner[j]==0:
            partner[i]=j
            partner[j]=i
            total+=solve()
            partner[i]=partner[j]=0
    return total
x = solve()
print(x)




fin.close()