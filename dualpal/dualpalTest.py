my_list1 = ["3 25"]
my_list2 = ["15 10000"]
my_list3 = []
my_list4 = []
my_list5 = []
my_list6 = []
my_list7 = []
#"""
openfile = open('dualpal.txt', 'w+')
for item in my_list1:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open("transform.txt","r"):
    listinha.append(line.strip())
print(listinha)
"""
