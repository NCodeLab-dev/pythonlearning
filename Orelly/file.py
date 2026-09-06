
#reading and checking if a string is present
"""
with open("data.txt") as file:
    file_data = file.read()

if "Python" in file_data:
    print(file_data)
    print("Python is present");
else:
    print("Python is not present")

"""
"""
#how to read file line by line
with open("data.txt") as file:
    n=0
    for each_line in file:
        n+=1
        #print(each_line)
        print(n,each_line.rstrip("\n"))
"""

#writing to a file
"""
with open("data.txt",mode="at") as file:
    char_added = file.write("hello narayan\n")
    print(char_added, "characters added to the file")

"""

