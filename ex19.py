# define the function with 2 arguments, cheese_count & boxes_of_crackers
cheese_count = int(input("Please enter number of cheeses: "))
boxes_of_crackers = int(input("Please enter number of crackers: "))

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxed of crackers!" % boxes_of_crackers)
	print ("Man that's enough for a party! \n")
	if cheese_count > 100:
		a = "normaal doen!"
		print (a.upper()*2)
		
cheese_and_crackers(cheese_count, boxes_of_crackers)
"""#print numbers directly after the function is called 	
print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

#give other variables a specific value
print ("Or, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

#the cheese_and_crackers function called with 2 variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too: ")
cheese_and_crackers(10+20, 5+6)

#make a combination of variables and values. The function still works.
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)"""