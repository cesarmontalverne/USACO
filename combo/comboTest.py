my_list1 = ["50","1 2 3","5 6 7"] #249
my_list2 = ["1", "1 1 1","1 1 1"] #1
my_list3 = ["2", "1 2 1", "2 1 2"]
my_list4 = []
my_list5 = []
file = "combo.txt"
#"""
openfile = open(file, 'w+')
for item in my_list3:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open(file,"r"):
    listinha.append(line.strip())
print(listinha)
"""