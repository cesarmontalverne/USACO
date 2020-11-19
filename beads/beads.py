"""
ID: ca6fqb1
LANG: PYTHON2
TASK: beads
"""
fin = open("beads.in", "r")
grouping = []
bs=fin.readline()
string = fin.readline().strip()
L1 = [string[0]]
L2 = [1]
for i in range(1,len(string)):
    if string[i-1] == string[i]:
        L2[-1]+=1
    else:
        L1.append(string[i])
        L2.append(1)
def group(indexFirst):
    if len(L1)<2:
        grouping.append([0,0])
        return 1
    if L1[indexFirst] == "w" and not indexFirst:
        s = indexFirst - 1
        e = indexFirst + 1
    else:
        s = indexFirst
        e = indexFirst
    i = 1
    while L1[s]==L1[s-i] or L1[s-i]=="w":
        i+=1
    i-=1
    n = i
    while L1[s-n]==L1[s-i] or L1[s-i]=="w":
        i+=1
    s-=i-1
    i = 1
    while L1[e%len(L1)]==L1[(e+i)%len(L1)] or L1[(e+i)%len(L1)]=="w":
        i+=1
    n = i
    while L1[(e+n)%len(L1)]==L1[(e+i)%len(L1)] or L1[(e+i)%len(L1)]=="w":
        i+=1
    e=(e+i-1)%len(L1)
    grouping.append([s,e])
    return e
e1 = group(0)-1
ef = e1+1
if len(L1)<2:
    e1 = ef+1
while e1<ef:
   ef = group(ef)
final = []
for i in range(len(grouping)):
   n = 0
   beg = grouping[i][0]
   end = grouping[i][1]
   if beg > end:
       end+=len(L1)
   while beg <= end:
       n+=L2[beg%len(L1)]
       beg+=1
   final.append(n)
with open("beads.out","w") as fout:
    fout.write(str(max(final))+"\n")


