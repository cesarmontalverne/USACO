my_list1 = ['5', '2 3 4 6 8'] #1
my_list2 = ['9','1 2 3 4 5 6 7 8 9']
my_list3 = ['7', '4 1 2 5 6 7 3'] #384
my_list4 = ["2", "1 2"]
my_list5 = []
file = "crypt1.txt"
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
