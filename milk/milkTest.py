my_list1 = ['100 5', '5 20', '9 40', '3 10', '8 80', '6 30']
my_list2 = [""]
my_list3 = []
my_list4 = []
my_list5 = []
my_list6 = []
my_list7 = []
#"""
openfile = open('milk.txt', 'w+')
for item in my_list1:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open("milk.txt","r"):
    listinha.append(line.strip())
print(listinha)
"""