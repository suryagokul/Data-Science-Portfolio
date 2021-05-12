import re

# Character Classes

#[abc] = match either a or b or c
matches = re.finditer('[abc]','hai buddy cu tmrw')

for match in matches:
    print(f"{match.group()} found at index {match.start()}")
print('*'*30)

#[^abc] = match except a,b,c
matches1 = re.finditer('[^abc]','hai buddy cu tmrw')

for match in matches1:
    print(f"{match.group()} found at index {match.start()}") 
print('*'*30)

#[a-zA-Z0-9] = matches all characters and 0-9 digits also     
alphanums = re.finditer('[^a-zA-Z0-9]',
                       'iamurfriend!mymailis xyz@yahoo.com')
for i in alphanums:
    print(i.group(), i.start(), i.end()) # end returns end+1
    
