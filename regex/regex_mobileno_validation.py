import re

no = input("enter > ")

match = re.fullmatch('[6-9][0-9]{9}',no)

if match!=None:
    print("valid mobile no")

else:
    print("not valid mobile no")

