#import specific arg functions from sys module 
from sys import argv
#define the arguments
script, filename = argv
#opened the file, filename is written by user
txt = open(filename)
#print statement with name of the file
print ("here's your file %r: " % filename)
#print the whole file
print (txt.read())
