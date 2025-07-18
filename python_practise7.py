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
