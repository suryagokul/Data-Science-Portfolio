import re
from urllib.request import urlopen

site = 'https://www.redbus.in/info/contactus' 

print("Opening site and Extracting...")

u = urlopen(site)

text = u.read()   # gives entire source of page i.e html/css/js so type is <class 'bytes'> 

#print(type(text))

all_matches = re.findall('[+91]+[0-9]{10}',str(text))       # returns all matches as an iterable (list)

for match in all_matches:
    print(match)