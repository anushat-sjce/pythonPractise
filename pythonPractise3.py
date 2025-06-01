def hello(name):
  print(f"Hello {name}")
name = "Ishaan and Anusha and Jay"
hello(name)

Country = "Australia"
Capital = "Canberra"
print(f"{Capital} is the capital of {Country}")



*************************************### Adding number and returning the value
def add(num1, num2):
 # print(num1 + num2)
  return num1+ num2
num1 = 64
num2 = 46
v = add(num1, num2)
print(v)

n = 23
********************************nested functions***************************
def test(n):
  n = 20
  print(n)

test(19)

def hello(name):
  print(f"Hello {name}")

def fav_city(city_name,name):
  hello(name)
  print(f"Welcome to {city_name}!!")

fav_city("Australia", "Arthi")


***************Strings and quotes and accessing each element***************

single_quoted_strings = 'Hello Anusha'
double_quoted_strings = "Hello Anusha"
triple_quoted_strings = '''Hello Anusha'''

print(single_quoted_strings)
print(double_quoted_strings)
print(triple_quoted_strings)

multi_lined_string = '''
this is my story
no one helps me at home for the house work
i am tired of working and giving food to all these people
i want to go out and take rest
God please help me'''


print(multi_lined_string)
print(" ")
multi_lined_string[:30]


triple_quoted_strings[-1]


"hello" + " " + "world" + " " + "Anusha Welcome "


#join
text1 = ("Anusha", "Ishaan", "Jay")
x = " ".join(text1)
print(x)

#strip
text = "www.come"
s = text.strip("w")
print(s) 

#split
text = "Hello welcome to learning python programming"
v = text.split()
print(v)


#strip, lower, upper, 
name = "anusha t das"
#name.upper()
#name.lower()
v = name.count("a")
print(v)

s = name.strip("sha")
print(s)

"hello" + " " + "world" + " " + "Anusha Welcome "

text = "I like bananas"
s = text.replace("bananas", "APPLES")
print(s)
