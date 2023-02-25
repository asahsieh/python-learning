# Accepting Arguments from Command Line
## use the `sys` module from the std lib
import sys

### $ python3 advanced_topics.py beau 39
### ['advanced_topics.py', 'beau', '39']
print(sys.argv)

### Assign argument to a variable and use the variable
#name = sys.argv[1]
#print("Hello " + name)

## You really would have to do a lot of work using this method
## because you really should validate the arguments 
## make sure the type is correct and you need to print feedback to the user
## if they're not using the program correctly

### Example code
### parser = argparse.ArgumentParser(
###     description='sum the integers at the command line')
### parser.add_argument(
###     'integers', metavar='int', nargs='+', type=int,
###     help='an integer to be summed')
### parser.add_argument(
###     '--log', default=sys.stdout, type=argparse.FileType('w'),
###     help='the file where the sum should be written')
### args = parser.parse_args()
### args.log.write('%s' % sum(args.integers))
### args.log.close()

import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

# Commands: 
# - $ python advanced_topics.py -c red
# - $ python advanced_topics.py -c # will return help and get an error 

# The parameter `choices` is to bound the valid choices
parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow'}, help='the color to search for')

args = parser.parse_args()

print(args.color)