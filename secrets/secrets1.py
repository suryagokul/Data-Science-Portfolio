import string,secrets

# taking all the characters and digits
alphabets = string.ascii_letters + string.digits           

# creating secret of length 10
for i in range(11):
    x = secrets.choice(alphabets)         # get any element from alphabets 
    print(''.join(x),end="")