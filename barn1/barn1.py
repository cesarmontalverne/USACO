"""
ID: ca6fqb1
LANG: PYTHON2
TASK: barn1
"""
fin = open("barn1.in","r")
m, s, c = list(map(int,fin.readline().strip().split(" ")))
cowlist = list(map(int,fin.read().strip().split("\n")))
cowlist.sort()
gaplist = [cowlist[i]-cowlist[i-1]-1 for i in range(1,c)]
toret = cowlist[-1]-cowlist[0]+1
gaplist.sort(reverse=True)
for i in range(m-1):
    if len(gaplist)<=i:
        break
    toret-=gaplist[i]
with open("barn1.out","w") as fout:
    fout.write(str(toret)+"\n")