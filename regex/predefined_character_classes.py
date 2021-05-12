import re

            # pre-defined Character Classes

# \s = get all space chars
for match in re.finditer('\s','char classes pre defined'):
    print(f"getting space character at index {match.start()}")
print()

# \S = except all space chars
for match in re.finditer('\S','char classes3!'):
    print(f"getting all characters except space {match.group()}")
print()
    
# \d = all digits
for match in re.finditer('\d','char42 classes3!'):
    print(f"getting all digits {match.group()}")
print()
    
# \D = all chars except digits
for match in re.finditer('\D','cls422'):
    print(f"getting all chars except digits {match.group()}")
print()
    
# \w = alphanum [a-zA-Z0-9]
for match in re.finditer('\w','char42 classes3!'):
    print(f"getting all alphanum {match.group()}")
print()

# \W = except alphanum [a-zA-Z0-9]
for match in re.finditer('\W','char@42!'):
    print(f"getting except alphanum {match.group()}")
print()

# . = matches each & every character including space
for match in re.finditer('.','a8c2 !@'):
    print(f"getting all alphanum {match.group()}")


