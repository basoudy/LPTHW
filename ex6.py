#explaining different types of people by using x as a variable.
#the number should not be previously mentioned.
#line 4 is a string inside a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#string inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y

#string inside a string
print "I said: %r." % x 
#string inside a string
print "I also said: '%s'." % y

hilarious = False
#string inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 