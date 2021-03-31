import argparse


parser = argparse.ArgumentParser(description="Arithmetic Operations")

# Positional Arguments  

parser.add_argument('number1', help='first number')

parser.add_argument('number2', help='second number')

parser.add_argument('operation', help='Operation todo',choices=['add','sub'])     # if other than choices are given then program terminates with invalid choice.

#we must provide positional arguments in command line Otherwise gives --> argument_parser.py: error: the following arguments are required: number1, number2,operation

args = parser.parse_args()

print(args.number1)            # all args is in str we need to convert them to perform operations

print(args.number2)

print(args.operation)

n1 = int(args.number1)

n2 = int(args.number2)

result = None

if args.operation == 'add':
    result = n1 + n2

elif args.operation == 'sub':
    result = n1 - n2

else:
    print("Invalid Operation")

print("Result : ",result)



