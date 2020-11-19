my_list = ["5"]

openfile = open('friday.txt', 'w+')
for item in my_list:
    openfile.write(str(item) + "\n")
openfile.close()