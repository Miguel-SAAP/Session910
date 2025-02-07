fp = open("text.txt", "r")
print(fp.read())
fp.close() #close i good practice; not needed

#same thing but more pythonic
with open("text.txt", "r") as fp:#this create the content
    print(fp.read())
print("we are done, the context closed by the ident")

#read from the same file, line by line
with open("text.txt", "r") as fp:
    line_number = 1
    for line in fp:
        #print(line, end="")
        print(f"Line {line_number}: {line.restrip()}")
        line_number += 1

