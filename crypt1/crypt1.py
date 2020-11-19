"""
ID: ca6fqb1
LANG: PYTHON2
TASK: crypt1
"""
fin = open("crypt1.in","r")
n = int(fin.readline().strip())
nums = list(map(int, fin.readline().strip().split(" ")))
def verify(num,l=3,time=0):
    num = str(num)
    n = len(num)
    if n>l:
        return False
    elif time==n:
        return True
    else:
        if not int(num[time]) in nums:
            return False
        return verify(num,l,time+1)
iter = 0
for dp in range(n):
    for ds in range(n):
        for tp in range(n):
            for ts in range(n):
                for tt in range(n):
                    tn = int(str(nums[tp]) + str(nums[ts]) + str(nums[tt]))
                    dn = int(str(nums[dp]) + str(nums[ds]))
                    if verify(nums[dp] * tn) and verify(nums[ds] * tn) and verify(tn * dn,4):
                        iter+=1
with open("crypt1.out","w") as fout:
    fout.write(str(iter) + "\n")