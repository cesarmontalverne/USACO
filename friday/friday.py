"""
ID: ca6fqb1
LANG: PYTHON2
TASK: friday
"""
fin = open('friday.in', 'r')
N = int(fin.readline())
occurrence = [0,0,0,0,0,0,0]
monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
def isLeap(year):
    return (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))
for y in range(1900, 1900 + N):
    for i in monthsDays:
        occurrence[day % 7] += 1
        if (i == 28):
            if isLeap(y):
                day += 29
        day += i
with open('friday.out', 'w') as fout:
    fout.write(str(occurrence[0]) + " " + str(occurrence[1]) + " " + str(occurrence[2]) + " " + str(occurrence[3]) + " " + str(occurrence[4]) +" " + str(occurrence[5]) + " " + str(occurrence[6]) + "\n")
