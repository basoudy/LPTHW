name = 'Bas Oudejans'
age = 22 # not a lie 
height = 74 # inches
weight = 180 # lbs
eyes = "green"
teeth = "white"
hair = 'blond'
poepkleur = 'bruin'

print "Lets's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
#poep praatje
print "Zijn poep is meestal %s, tenzij hij rode kool heeft gegeten." % poepkleur

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print round (1.7333333)
