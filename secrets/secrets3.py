import secrets as s

no_below_50 = s.randbelow(50)

value_below_15 = s.randbits(4)            # 1111 = 15

print(f"Random number below 50 is {no_below_50} \nRandom number below 4bits is  {value_below_15} ")
print('*'*30)

# generating secure tokens for applications such as password resets, hard-to-guess URLs etc.

token1 = s.token_bytes()                   
token2 = s.token_bytes(10)         # random byte string containing nbytes
  
print("Default token bytes ",token1)
print("Token bytes of 10 ",token2)
print('*'*30)

# hexa decimal token
token_hex1 = s.token_hex()
token_hex2 = s.token_hex(2)


print("Default hex token ",token_hex1)
print("Hexa decimal token of bytes 2 ",token_hex2)
print('*'*30)


# token_urlsafe()

'''generating a random URL-safe text string containing nbytes random bytes. This is suitable for password recovery applications.
Example : Generate a hard-to-guess temporary URL containing a security token.
'''

url = "http://www.facebook.com/password/reset=" + s.token_urlsafe()

print("Safe Url is : ",url)