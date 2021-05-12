import re

# regex object
pattern = re.compile("@gmail.com")

print(pattern)

# returns all matches as an iterator
matches = pattern.finditer("hello hai my name is xyz and mail is abcde@gmail.com, support@gmail.com")

print(matches)

# or we can also do without compile as re.finditer('@gmail..',"hello hai....")

for match in matches:
    print("pattern is ", match.group(),match.start(), match.end())
