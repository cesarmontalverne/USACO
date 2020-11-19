"""
ID: ca6fqb1
LANG: PYTHON2
TASK: milk2
"""
fin = open("milk2.txt","r")
n = int(fin.readline().strip())
times = []
for i in range(n):
    a = fin.readline().split()
    b = int(a[0])
    c = int(a[1])
    times.append([b,c])
times.sort()
L = [[times[0][0],times[0][1]]]
index = times[0][1]
maxTime,maxRest = 0,0
for i in range(n):
    iter = 0
    while iter<len(L):
        if times[i][1] > L[iter][1] and times[i][0]<=L[iter][1]:
            L[iter][1]=times[i][1]
            if times[i][0]<L[iter][0]:
                L[iter][0] = times[i][0]
        elif (times[i][0])<=L[iter][0] and (times[i][1])>=L[iter][0]:
            L[iter][0] = (times[i][0])
        else:
            if [(times[i][0]),(times[i][1])] not in L:
                L.append([(times[i][0]),(times[i][1])])
        if L[iter][1] - L[iter][0] > maxTime:
            maxTime = L[iter][1] - L[iter][0]
        if iter < len(L) -1  and L[iter+1][0]-L[iter][1]>maxRest and L[iter+1][0]>index:
            maxRest = L[iter + 1][0] - L[iter][1]
        iter+=1
with open("milk2.out","w") as fout:
    fout.write(str(maxTime)+" "+str(maxRest)+"\n")
