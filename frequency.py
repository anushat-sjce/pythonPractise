from collections import Counter

s1 = [1,2,3,4,2,2,1,1]
num = (Counter(s1))
print(num)

s2 =["anusha", "ishaan", "jay", "ishaan"]
c1 = Counter(s2)
print(c1)
#print(list(c1)) 

x = max(c1.values())
print(x)
highest_key = c1.most_common(1)[0][0]
print(highest_key)


s3 = "anusha"
y = (Counter(s3))
print(y.most_common(1)[0][0])
