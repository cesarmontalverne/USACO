my_list = ["29","wwwbbrwrbrbrrbrbrwrwwrbwrwrrb "]

openfile = open('beads.txt', 'w')
for item in my_list:
    openfile.write(str(item) + "\n")
openfile.close()