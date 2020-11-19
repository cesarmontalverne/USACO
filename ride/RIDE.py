"""
ID: ca6fqb1
LANG: PYTHON2
TASK: ride
"""
def decode(inp):
    number = 1
    for letter in inp:
        number *= (ord(letter)-64)
    return number % 47
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
comet, group = fin.read().splitlines()
result = "GO\n" if decode(group) == decode(comet) else "STAY\n"
fout.write(result)
fout.close()

