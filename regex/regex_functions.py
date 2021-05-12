import re

'''
functions of regex

    match,fullmatch,compile,search,finditer,findall,sub,subn,split
'''
# match = To check pattern is at the begining or not.
# if doesn't match returns None
print(re.match('a','fdaff')) # None

# fullmatch = to check full pattern is matched or not
print(re.fullmatch('string','string'))    # returns match object

# compile = to create regex object
p = re.compile('patterns')
print(p)       

# search = returns first occurence if multiple otherwise None
s = re.search('why','why python? why it is popular?')
print(s.group())

# finditer = returns iterator of all matches
matches = re.finditer('am','time we went is 9am and returns at 11am')
for match in matches:
    print(match.group(),"at",match.start(),"th index")

# findall = returns all matches in list
all_matches = re.findall('am','time we went is 9am and returns at 11am')
print(all_matches)


# sub = substitution or replacement
s = re.sub('\d','#','a92fw5') 
print(s)  # replacing all digits with '#' a##fw#.

# subn = returns tuple of (string_after_replaced, no of replacements)
sn = re.subn('\d','#','a92fw5')
print("result string ",sn[0])
print("No of replacements ",sn[1])

# split = splits based on given character & returns list
l = re.split('/', '14/07/2001')
print(l)
