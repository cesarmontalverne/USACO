"""
ID: ca6fqb1
LANG: PYTHON2
TASK: milk
"""
fin = open("milk.in","r")
qntneed, n = list(map(int, fin.readline().strip().split(" ")))
farmers = [list(map(int,fin.readline().strip().split(" "))) for i in range(n)]
farmers.sort()
iter,cashspent = 0,0
def greedy(qnt,iter=0):
    global cashspent
    if qnt == 0:
        return
    elif qnt>=farmers[iter][1]:
        cashspent += farmers[iter][0] * farmers[iter][1]
        return greedy(qnt-farmers[iter][1],iter+1)
    else:
        cashspent += farmers[iter][0] * qnt
        return
greedy(qntneed)
with open("milk.out","w") as fout:
    fout.write(str(cashspent)+"\n")
