with open("sample1.py", "r") as file:
    #text = file.readline()
    full_text = file.read()
    #print(text)
    print("newline")
    print(full_text)
    print(file.mode)
    print(file.name)

    print(file.closed)
    file.close()


with open("example.txt", "w") as file1:
          file1.write("Hello how are you \n")
          file1.write("I am doing good\n")
          file1.close()

with open("example.txt", "r") as file2:
         print(file2.read())

with open("example2.txt", "w") as file3:
        file3.write("Am Anusha T\n")
        file3.write("Welcome to python programming\n")
        file3.write("I got a job in Microsoft")
        file3.close()

with open("example2.txt", "r") as file4:
        for line in file4:
                print(line)
