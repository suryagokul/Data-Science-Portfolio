# In the positional arguments there is some ambiguity because if we change order of number1 and number2 in cmd line then result may also change.

#To solve this we need Optional arguments (flags) which are specified with --.

import argparse

import logging

parser = argparse.ArgumentParser()

parser.add_argument('--number1', help='first number')

parser.add_argument('--number2', help='second number')

parser.add_argument('--operation', help='Operation todo',choices=['add','sub'])

args = parser.parse_args()

print("First Argument is : ",args.number1)


logging.basicConfig(filename='log_arguments.txt',level=logging.INFO,filemode='a',format='%(asctime)s:%(levelname)s:%(arguments)s',datefmt='%d/%m/%Y %H:%M:%S %p')

# file mode = 'w' for override every time

# file mode = 'a' for appending every time in log.txt file

logging.info("INFO", extra = {'arguments': ' '.join( ['Arguments passed are : ', args.number1, args.number2, args.operation] ) } )


