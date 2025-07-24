list1 = ["Hello welcome to Bengaluru\n", "Kannada is our mother tongue\n", "We like idli vada sambar\n"]
with open("example3.txt", "w") as writefile1:
    for lines in list1:
        print(lines)
        writefile1.write(lines)
    writefile1.close()

print("####Reading example3.txt file line by line")
with open("example3.txt", "r") as readfile:
    for line in readfile:
     print(line)
