#amount of drivers
cars = 100
#amount of seats in a car (does not differ with floating point)
space_in_a_car = 4
#available drivers at the moment.
drivers = 30
passengers = 90
#cars not driven using space to name variables
cars_not_driven = cars - drivers
#because it is only allowed to drive a car for 1 person
cars_driven = drivers
#total amount of passengers that could be removed
carpool_capacity = cars_driven * space_in_a_car
#total amount of people in a car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

x = 5
y = 7 * 4
times = x * y
sum = x + y

print times
print sum