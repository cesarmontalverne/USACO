my_list1 = ['4 50 18', '3', '4', '6', '8', '14', '15', '16', '17', '21', '25', '26', '27', '30', '31', '40', '41', '42','43'] #25
my_list2 = ['1 200 8', '101', '105', '102', '106', '103', '107', '104', '99'] #9
my_list3 = ['50 200 10', '18', '69', '195', '38', '73', '28', '6', '172', '53', '99']
my_list4 = []
my_list5 = []

#"""
openfile = open('barn1.txt', 'w+')
for item in my_list3:
    openfile.write(str(item) + "\n")
openfile.close()

"""
listinha = []
for line in open("barn1.txt","r"):
    listinha.append(line.strip())
print(listinha)
"""