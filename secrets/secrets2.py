import string,secrets

# taking all the characters and digits
alphabets = string.ascii_letters + string.digits + string.punctuation         

while True:
    x = ''.join(secrets.choice(alphabets) for i in range(11))
    if (any(j.islower() for j in x) and any(j.isupper() for j in x) and sum(c.isdigit() for c in x)>=3) and any(not c.isalnum() for c in x):        
        print(x)
        break