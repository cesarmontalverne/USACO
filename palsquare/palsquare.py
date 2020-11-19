"""
ID: ca6fqb1
LANG: PYTHON2
TASK: palsquare
"""
fin = open("palsquare.in","r")
base = int(fin.readline().strip())
listnewbase,listation, listpossnewnums = [],[],["A","B","C","D","E","F","G","H","I","J"]
s = ""
for i in range(base):
    if i<10:
        listnewbase.append(str(i))
    else:
        listnewbase.append(listpossnewnums[i%10])
def transbase(n,time=0):
    global s
    if not time:
        s = ""
    if n//base**time == 0:
        return s
    else:
        s = listnewbase[(n//base**time)%base] + s
        return transbase(n,time+1)
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
def checkpali(n=1):
    sq = n*n
    tsq = transbase(sq)
    if n>300:
        return
    else:
        if actcheck(tsq):
            listation.append([transbase(n),tsq])
        return checkpali(n+1)
checkpali()

with open("palsquare.out","w") as fout:
    for item in listation:
        fout.write(item[0]+" "+item[1]+"\n")


