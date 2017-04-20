#import sys module with function argv
from sys import argv
#define specific variables to functions
script, input_file = argv
#define function print_all
def print_all(f):
	print (f.read())
#define rewind function, not sure what it does actually 	
def rewind(f):
	f.seek(0)
#define function to print one line everytime		
def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines: ")

#call on print_a_line function. Current line is extended with 1 after being run.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)	