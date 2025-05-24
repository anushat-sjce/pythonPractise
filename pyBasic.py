# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

name = input("Enter name")
print("Hello", name);
standard, section = input("Enter class and grade").split()
print(standard, "and", section)

age = input("Enter age")
age = int(age)
print(age)

if age < 0 : 
        print("You are a baby")
elif age > 3 and age < 6 :
        print("You are child")
elif age > 6 and age < 18 :
        print ("You are student")
else:
        print("You are adult")
        
age = float(input("Enter numbers"))
print(age)
