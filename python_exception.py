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
