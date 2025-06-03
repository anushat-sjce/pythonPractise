try: 
  print(x)
except:
  print("A name error exception occured")


try:
  y = 10/0
except:
  print("Zerodivision error occured")

try:
  y = 5 + "Hello"
except:
  print("Naming exception occured")


try :
  z = int("hello")
except:
  print("Type conversion exception occured")
************************************************************************8file handling in python*************************************

with open("my_csv.txt", "w") as f:
  f.write("Hello welcome to pthon file handling\n")
  f.write("this is line no 2")


with open("my_csv.txt", "r") as f:
  print(f.read())
************************************************************************csv file operations*****************************************8
import pandas as pd

data = {'Column 1': ['Row 1 Data 1', 'Row 2 Data 1'],
        'Column 2': ['Row 1 Data 2', 'Row 2 Data 2']}
df = pd.DataFrame(data)

df.to_csv('my_csv_file.csv', index=False)

  pd.read_csv;("my_csv_file.csv")


student = {"name":"Anusha", "age":"36"}
#print(student)
print(student)
student["name"] = "Sunidhi T Das"
student
for key in student:
  print(key)
for value in student:
  print(student[value])

for value in student:
  print(student[value])

***************************************************************************************************************************88
for k, v in student.items():
  print(k, v) 

if "Name" in student:
  print("True")
else:
  print("false")


for k in student:
  if k == "age":
    print(student[k])


*********************************************************************************
if "D" == student["C"]:
  print(v)
else:
  print("Nothing")

*****************************
for k in student:
  print(k)

*********************************

for val in student.values():
  print(val)


for keys, values in student.items():
  print(keys, values)

if "Z" in student.keys():
  print("Yes exists")
else:
  print("Nope")


del student["Age"]
print(student)


set1 ={ 1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

tuple1 = (1,2,3,1,2,3)
set(tuple1)
set1 = {1,2,1,2,1,2}
set(set1)

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
print(tuple1 + tuple2)

tuple3 = (5 ,6 ,7)
print(tuple3 * 2)

a,b,c = (1, 2, 3)
print(a)
print(b)
print(c)

a,b,c = (1, 2, 3)
print(a)
print(b)
print(c)


# Counting elements in a tuple
tuple1 = (1, 2, 2, 3, 4, 2)
count = 0

for i in tuple1:
  if(i == 2):
    count = count + 1

print(count)

tuple1 = ('a', 'b', 'c', 'd', 'b')
index = 0

for i in tuple1:
  index = index + 1
  if i == 'b':
    print(index)

set(tuple1)

list1 = [1,2,3,4,5]
tuple1 = tuple(list1)

print(tuple1)

colors = ('red', 'green', 'blue', 'yellow')
i = 0;
for count in colors:
  i = i+ 1
print(i)


tuple1 = ('apple', 'banana', 'cherry')
if 'banana' in tuple1:
  print("Yes, it is")
else:
  print("No")
  \

coordinates = (100, 200)
x,y = 100, 200
print(x)
print(y)


my_tuple = ('a', 'b')
new_tuple = my_tuple * 3
print(new_tuple)

tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)

set1 ={ 1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

tuple1 = (1,2,3,1,2,3)
set(tuple1)
