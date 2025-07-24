import pandas as pd

#df = pd.read_csv('data.csv')
data1 = [10,20,304,506,506,73,73]
data = ["a", "b", "c", "a", "b", "c"]
x = pd.Series(data)
print(x)
print("\n")
print("size :", x.size)
print("third element :",x[2])
print("print 1st till 3rd element :", x[1:4])
print("Sum of all elements :", x.sum())
print("Unique number: ", x.unique())
