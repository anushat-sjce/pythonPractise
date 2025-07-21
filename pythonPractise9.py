def summation(a, b):
    sum1 = a + b
    return sum1
    
total = summation(10, 57)
print(total)

length = len("Hello world")
print(length)

length1 = len([1,2,3,4,5,6,7,3,5,1,4,5])
print(length1)

total = max([23,64565,235,7567,7645])
print(total)

def add_element(b, x):
    b.append(x)

def remove_element(c, y):
    c.remove(y)

my_list= []
print(my_list)
my_list.append(12)

my_list.append(21)
my_list.append(34)
my_list.append(56)
my_list.append(78)
print(my_list)

my_list.remove(78)
print(my_list)
add_element(my_list, 100)
print(my_list)
remove_element(my_list, 12)
print(my_list)


def multiply(a, b):
    result = a * b 
    return result
    
    
res = multiply(2, "anusha")
print(res)

'''
passing lists to the functions
'''

def print_elements(*args):
    for i in args:
        print(i)

print_elements((1,5,3,7,445,3,4,7))


def print_dict(**args):
    for i in args:
        print(i)
    for values in args.values():
        print(values)
    
print_dict(Canada="Ontario", India="New Delhi")

def addItems(list1):
    list1.append("Three")
    list1.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)

def division(a, b):
    result = a/ b
    return result
res = division(10,2)
print(res)


'''
concatenate the lists and tuples
'''

def add_elements(list1):
    list1.append(10)
    list1.append(20)
    return list1
    
list1 = [45, 89]
new_list = add_elements(list1)
print(new_list)


def add_tuples(tup1):
    tup2 = ("Sunidhi", "Das", "Girija")
    tup3 = tup2 + tup1
    return tup3
    
tup1 = ("asnusha","ishaan", "jay", 25)
new_tup = add_tuples(tup1)
print(new_tup)



'''
concatenate the lists and tuples
'''

def add_elements(list1):
    list1.append(10)
    list1.append(20)
    return list1
    
list1 = [45, 89]
new_list = add_elements(list1)
print(new_list)


def add_tuples(tup1):
    tup2 = ("Sunidhi", "Das", "Girija")
    tup3 = tup2 + tup1
    return tup3
    
tup1 = ("asnusha","ishaan", "jay", 25)
new_tup = add_tuples(tup1)
print(new_tup)  

def count(str, passkey):
    words = []
    dict1 = {}
    words = str.split()

for key in words:
        if(key == passedkey):
            dict1[key] = words.count(key)   
    #step5: Print the dictionary
print("Total Count:",dict1)
    
passkey = "little"
string1 = {"Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"}
count(string1)
