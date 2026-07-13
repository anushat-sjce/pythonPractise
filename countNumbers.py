from collections import Counter

a1 = [1,2,3,1,2,3,4]
x = (Counter(a1))
print(x)

for i in a1:
    if x[i]== 1:
        print(i)
