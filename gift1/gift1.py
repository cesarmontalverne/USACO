"""
ID: ca6fqb1
LANG: PYTHON2
TASK: gift1
"""
a = 1
fin = open("gift1.in", 'r')
fout = open("gift1.out",'w')
nFriends = int(fin.readline().strip())
friendList = [fin.readline().strip() for i in range(nFriends)]
friendDic = {friendList[i]: 0 for i in range(nFriends)}

while (True):
    giver = fin.readline().strip()
    if giver == "":
        break
    b = fin.readline().strip().split()

    given = int(b[0])
    nOfReceivers = int(b[1])
    if nOfReceivers>0:
        subbed = given - given % nOfReceivers
        amountReceived = subbed // nOfReceivers
        friendDic[giver] -= subbed
        for i in range(nOfReceivers):
            friendDic[fin.readline().strip()] += amountReceived

for name in friendList:
    fout.write("{} {}\n".format(name, friendDic[name]))
