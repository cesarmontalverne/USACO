"""
ID: ca6fqb1
LANG: PYTHON2
TASK: dualpal
"""
fin = open("dualpal.in","r")
N,S = map(int,fin.readline().strip().split(" "))
s,finlist ="",[]
def transbase(num,base,time=0):
    global s
    if not time:
        s = ""
    if num//base**time == 0:
        return s
    else:
        s = str((num//base**time)%base) + s
        return transbase(num,base,time+1)
def actcheck(tsq, time2=0):
    if 2 * (time2 + 1) >= len(tsq):
        if tsq[time2] == tsq[-(time2 + 1)]:
            return True
        else:
            return False
    else:
        if tsq[time2] == tsq[-(time2 + 1)]:
            return actcheck(tsq, time2 + 1)
        else:
            return False
def basecheck(num,base=2,coun=0):
    tsq = transbase(num,base)
    if coun == 2:
        return True
    elif base > 10:
        return False
    else:
        if actcheck(tsq):
            coun+=1
        return basecheck(num,base+1,coun)
count = 0
while count < N:
    if basecheck(S+1):
        finlist.append(S+1)
        count+=1
    S+=1
with open("dualpal.out","w") as fout:
    for item in finlist:
        fout.write(str(item)+"\n")