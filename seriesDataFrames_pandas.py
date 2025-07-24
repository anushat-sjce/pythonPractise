
#Series 
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

#DataFrame
import pandas as pd

#df = pd.read_csv('data.csv')
#data1 = [10,20,304,506,506,73,73]
data = {"Name":["Anusha","Sunidhi", "Ishaan","Jay"], "Age":[36,28,6,35],"DOB":[1989, 1997, 2018, 1990]}

df = pd.DataFrame(data)
df.to_csv("sample.csv",index = False)
print(df)
print("\n")
print(df['Name'], "\n") 
#print(df['Age'] > 6)
#print("\n", df.iloc[2])
print("\n", df[2:3])
x = print(df.Age)
print(x >10)


#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df
