"""
ID: ca6fqb1
LANG: PYTHON2
TASK: wormhole
"""
fin = open("wormhole.in","r")
N = int(fin.readline().strip())
cord = [list(map(int,fin.readline().strip().split(" "))) for i in range(N)]
fin.close()
X = [0]+[cord[i][0] for i in range(N)]
Y = [0]+[cord[i][1] for i in range(N)]
partner = [0 for i in range(N+1)]
nextright = [0 for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if X[j]>X[i] and Y[j]==Y[i]:
            if nextright[i]==0 or X[j]<X[nextright[i]]:
                nextright[i]=j
def cicle():
    for start in range(1,N+1):
        pos = start
        for j in range(N):
            pos = nextright[partner[pos]]
        if pos!=0:
            return True
    return False
def makepar():
    total=i=0
    for i in range(1,N+1):
        if partner[i]==0:
            break
    if i==N:
        return cicle()
    for j in range(i+1,N+1):
        if partner[j]==0:
            partner[i]=j
            partner[j]=i
            total+=makepar()
            partner[i]=partner[j]=0
    return total
fout = open("wormhole.out","w+")
fout.write(str(makepar())+"\n")
fout.close()