# Use the split function to split the string by the "\s"
s2 = "Hello welcome to India"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)
**************************************************************************************

pattern = r"\W"  # Matches any non-word character
text = "Hello!!, wo, rld!"
matches = re.findall(",", text)

print("Matches:", matches)

*****************************************************************************************
import re
name1 = "Welcome Anusha as a Data scientist, at Microsoft"
result = re.search('Anusha', name1)
#print(result)

if(result):
    print("Match found")
else :
    print("Match not found")

****************************************************************************
name = "the bodyguard is a policeman"
split_string = name.split()
split_string

*************************************************************************

b= "HELLO NEHA"
b.find('HA')

*****************************************************************88
name= "hello NIDHI"
name
b= name.replace('NIDHI', 'NEHA')
b

*********************************************************************8

b = name.lower()
print(b)

*************************************************************
b = name.upper()
print(b)

****************************
