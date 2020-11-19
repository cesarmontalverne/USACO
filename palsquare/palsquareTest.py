my_list1 = [10]
my_list2 = [5]
my_list3 = [15]
my_list4 = [20]
my_list5 = [2]
my_list6 = []
my_list7 = []
#"""
openfile = open('dualpal.txt', 'w+')
for item in my_list5:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open("transform.txt","r"):
    listinha.append(line.strip())
print(listinha)
"""