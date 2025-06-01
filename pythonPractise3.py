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
