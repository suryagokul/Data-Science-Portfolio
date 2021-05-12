import re

            #  Quantifiers

def quantifier_plus(string):
    '''match pattern i.e a6 be must & then [a-zA-Z0-9#]
       be atleast one time otherwise gives None.'''

    match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]+', string)
    print("full match for quantifier +") if match!=None else print("Not matched for quantifier +")

def quantifier_star(string):
    '''match pattern i.e a6 be must & then [a-zA-Z0-9#] 
    can repeat any no of times including zero times also.'''
    
    match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*', string)
    print("full match for quantifier *") if match!=None else print("Not matched for quantifier *")
    
def quantifier_qmark(string):
    '''atmost one a i.e either one or zero no of a's if multiple 
       takes separately as individual ''' 
    
    match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]?', string)
    print("full match for quantifier ?") if match!=None else print("Not matched for quantifier ?")


def repeat_ntimes(string):
    '''a{n} exactly n no of a's in this case [a-zA-Z0-9#] must repeat exact 2 times ''' 
    
    match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]{2}', string)
    print("full match for quantifier {}") if match!=None else print("Not matched for quantifier {}")

def repeat_mntimes(string):
    '''a{m,n} {min m no of a's,max n no of a's}  in this case [a-zA-Z0-9#] can repeat max 2 times,1time or zero times ''' 
    
    match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]{0,2}', string)
    print("full match for quantifier {m,n}") if match!=None else print("Not matched for quantifier {m,n}")
    
def startswith():
    match = re.match('^hai','hai hello')
    if match!=None:
        print("startswith hai")
    else:
        print("not startswith hai")

def endswith():
    match = re.finditer('$thanku','hai hello thanku')
    if match!=None:
        print("endswith thanku")
    else:
        print("not endswith thanku")

    
string = input("enter full string  >> ")

# match exact pattern i.e a6a/b3z..
match = re.fullmatch('[a-k][0369][a-zA-Z0-9#]', string)
print("full match") if match!=None else print("Not matched")
quantifier_plus(string)
quantifier_star(string)
quantifier_qmark(string)
repeat_ntimes(string)
repeat_mntimes(string)
startswith()
endswith()
