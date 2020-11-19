"""
ID: ca6fqb1
LANG: PYTHON2
TASK: milk2
"""
import operator
fin = open("milk2.in","r")
n = int(fin.readline().strip())
times = []
for i in range(n):
    a = fin.readline().split()
    times.append([int(a[0]),int(a[1])])
times.sort()
start,end = times[0]
rang = []
consec,inter,continuity =[end-start],[0],times[0][1]
index = 0
for i in range(1,n):
    if times[i][1]>=continuity:
        continuity = times[i][1]
        if times[i][0] <= times[index][1]:
            end = times[i][1]
        else:
            rang.append([start,end])
            consec.append(end-start)
            consec.append(float("0."+str(index)))
            start = times[i][0]  #change start
            inter.append(start-end) #start of i but end of (i-1) - check other comments
            end = times[i][1] #change end
        index = i
        if not n-i-1:
            rang.append([start, end])
            consec.append(end - start)

with open("milk2.out","w") as fout:
    fout.write(str(max(consec))+" "+str(max(inter))+"\n")