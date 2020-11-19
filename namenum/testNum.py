my_list0 = ["4734"]
my_list1 = ["23325256"]
my_list2 = ["463373633623"]
#"""
openfile = open('namenum.txt', 'w+')
for item in my_list2:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open("dict.txt","r"):
    listinha.append(line.strip())
print(listinha)
"""
