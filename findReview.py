string_var = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
to_lower = string_var.lower()
#print(to_lower)

clean_string = to_lower.replace("!"," ").replace(","," ").replace(".", " ").replace("?"," ")
x = (clean_string.split())
unique_ele = set(x)
print(x)
print(unique_ele)

freq = {}

for word in unique_ele:
    freq[word] = x.count(word)

print(freq)

for key in freq:
    if(key == "lorem"):
        print(freq['lorem'])
