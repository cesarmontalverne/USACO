"""
ID: ca6fqb1
LANG: PYTHON2
TASK: transform
"""
fin = open("transform.in","r")
n = int(fin.readline().strip())
era = [fin.readline().strip().split() for a in range(n)]
eh = [fin.readline().strip().split() for b in range(n)]
freqJcres = "j"
freqJdec = "n-j-1"
freqIcres = "i"
freqIdec = "n-i-1"
#caso 1, 90 graus //era[iter][0][i%n] == eh[i%n][0][n-iter]
def func(primeiro, segundo, toret, terceiro = "i", quarto = "j"):
    global codered
    codered = False
    for i in range(n):
        for j in range(n):
            if not era[eval(primeiro)][0][eval(segundo)] == eh[eval(terceiro)][0][eval(quarto)]:
                codered = True
                break
        if codered:
            break
    if codered:
        return 7
    return toret

list2 = [
    func(freqJdec,freqIcres, 1),
    func(freqIdec, freqJdec, 2),
    func(freqJcres, freqIdec, 3),
    func(freqIcres, freqJdec, 4),
    func(freqJdec,freqIcres,5,freqIcres, freqJdec),
    func(freqIdec,freqJdec,5,freqIcres, freqJdec),
    func(freqJcres,freqIdec,5,freqIcres, freqJdec),
    func(freqIcres,freqJdec,6)
]


with open("transform.out","w+") as fout:
    fout.write(str(min(list2))+"\n")
