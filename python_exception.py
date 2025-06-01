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
