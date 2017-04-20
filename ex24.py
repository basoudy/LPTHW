#easy print statement
print ("Let's practice everything.")
#put a sentence in single brackets instead of double. Why only one blackslash?
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

#variable poem between """ and used a lot of tabs and newlines
poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print ("-------------")
print (poem)
print ("-------------")
#define variable five based on calculations
five = 10 - 2 + 3 - 6
#print the variable to see if it actually is 5
print ("This should be five: %s" % five)
#define a function named secret_formula. 
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
#define starting point	
start_point = 10000
#define that secret_formula is same as beans, jars, crates (so no longer jelly_beans) 
#start_point is equal to started as well.
beans, jars, crates = secret_formula(start_point)
#print all the assigned values 
print ("With a starting point of: %d" % start_point)
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
#new start_point and print all of these values
start_point = start_point / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))