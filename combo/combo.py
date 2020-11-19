"""
ID: ca6fqb1
LANG: PYTHON2
TASK: combo
"""
fin = open("combo.in","r")
N = int(fin.readline())
farcom = list(map(int,fin.readline().strip().split(" ")))
mastercom = list(map(int,fin.readline().strip().split(" ")))
set = set()
def funca(lis,time1=1,time2=1,time3=1):
    set.add(str((lis[0]+5-time1)%(N)) +" "+ str((lis[1]+5-time2)%(N))+" "+ str((lis[2]+5-time3)%(N)))
    if time1 == 5 and time2 == 5 and time3 == 5:
        return
    elif time2 == 5 and time3 == 5:
        funca(lis,time1+1)
    elif time3==5:
        funca(lis,time1,time2+1)
    else:
        funca(lis,time1,time2,time3+1)
funca(farcom)
funca(mastercom)
with open("combo.out", "w") as fout:
    fout.write(str(len(set))+"\n")