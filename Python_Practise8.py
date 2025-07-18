set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

list1 = ["anusha", "ishaan", "jay", "sunidhi","anusha"]
print(list1)
set2 = set(list1)
print(set2)

A = set(["qqqq", "rrrr", "gggg", "qqqq"])
print(A)
A.add("eeee")
print(A)
A.remove("rrrr")
print(A)
x = "ggg" in A
print(x)

A1 = set(["anusha", "ishaan", "jay"])
A2 = set(["anusha", "ishaan"])

A3 = A1 & A2
A4 = A1.difference(A2)
A5 = A1.union(A2)
A6 = A4.issuperset(A1)
print(A6)
print(A5)
print(A4)
print(A3)

B = set(['rap','house','electronic music', 'rap'])
print(B)
