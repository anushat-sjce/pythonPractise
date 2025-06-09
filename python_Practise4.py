import pandas as pd

dict1 = {'people':['p1', 'p2', 'p3'], 'Age':[20, 30, 40]}
dict1

df = pd.DataFrame(dict1)

pd.read_excel("test1.xlsx")

df.to_csv("sample.csv", index = False)

pd.read_csv("sample.csv")

df['Age'].sum()
df['people']
df[df["Age"] >= 30]

import matplotlib.pyplot as plt
#Hours vs Marks
#Hours : 2, 4, 6, 8, 10
#Marks : 21, 38, 64, 85, 98

hours = [2, 4, 6, 8, 10]
math_marks = [21, 38, 64, 85, 98]
science_marks = [ 10, 15, 19, 25, 35]

plt.scatter(hours, math_marks, label = "Math")
plt.scatter(hours, science_marks, label = "Science")
plt.xlabel("Hours spent")
plt.ylabel("Marks scored")
plt.title("Students data of hours spent vs marks scored")
plt.legend()
plt.show()
