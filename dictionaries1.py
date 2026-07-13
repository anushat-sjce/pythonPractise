import re
from collections import Counter

student = {
    "name": "Anusha",
    "marks": 90
}

student["age"] = 25
student["mother"] = "Anusha T"
student["father"] = "Jay"

passage = "Hello good morning dear students. Welcome to the class of 2026-2027 batch. Our school is very much privilged to welcome you all students for this academic year. Once again, a grand welcome to all the students present here."
 
words = re.findall(r'\b\w+\b', passage.lower())
print(Counter(words))
