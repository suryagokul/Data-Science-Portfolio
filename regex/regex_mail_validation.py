import re
mail = input("enter > ")
match = re.fullmatch('[a-zA-Z0-9._]+@[a-zA-Z0-9]+[.][a-z]+',mail)
print(match)
if match!=None:
    print("valid mail id")
else:
    print("not valid email id")