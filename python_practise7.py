nventory_store = {}


print(Inventory_store)
Inventory_store["Product Name"] = "Mobile Phone"
Inventory_store["Product Quantity"] = 5
Inventory_store["Product price"] = 20000
Inventory_store["Product Release Year"] = 2020


print(Inventory_store)
for k in Inventory_store:
    res = k
    print(res)
    
for val in Inventory_store.values():
    print(val)
    
for keys in Inventory_store.keys():
    if (keys == 'Product Name'):
        print("Found")
        break
    else :
        print("Not found")
        

for keys in Inventory_store.keys():
    if (keys == 'Product Release Year'):
        del Inventory_store[keys]
        break
print(Inventory_store)


A = [1,2,2,1]
B = [2,2,1,1,2]
if (sum(A) == sum(B)):
    print("True")
else:
    print("False")
    
    

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

x = album_set1.issubset(album_set3)
print(x)

y = album_set1.issuperset({"Back in Black", "AC/DC"})
print(y)

A = set(['rap','house','electronic music', 'rap'])
print(A)
