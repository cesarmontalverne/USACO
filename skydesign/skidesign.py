"""
ID: ca6fqb1
LANG: PYTHON2
TASK: skidesign
"""
fin = open("skidesign.in","r")
n = int(fin.readline().strip())
heights = list(map(int,[fin.readline().strip() for i in range(n)]))
fin.close()
heights.sort()
sumf = 0
difs = [0 for j in range(n)]
h = heights[-1] - heights[0]
def evade():
    global difs, sumf
    if h-difs[0]-difs[-1]<=17:
        return
    else:
        difs1 = difs[:]
        difs2 = difs[:]
        sum1 = sum2 = 0
        for i in range(n):
            if heights[0]+difs[0]<heights[i]+difs[i]:
                break
            difs1[i]+=1
        for j in range(n-1,-1,-1):
            if heights[j]-difs[j]<heights[-1]-difs[-1]:
                break
            difs2[j]+=1
        for k in range(n):
            sum1+=difs1[k]**2
            sum2+=difs2[k]**2
        if sum1<=sum2:
            difs = difs1[:]
            sumf = sum1
        else:
            difs = difs2[:]
            sumf = sum2
        evade()
evade()
fout = open("skidesign.out","w+")
fout.write(str(sumf)+"\n")