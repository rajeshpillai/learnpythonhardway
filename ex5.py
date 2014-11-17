# Exercise 5: More Variables and Printing
# Now we'll do even more typing of variables and printing them out. This time we'll use something called a "format string." 

# Every time you put " (double-quotes) around a piece of text you have been making a string. A string is how you make something 
# that your program might give to a human. You print strings, save strings to files, send strings to web servers, and many other things.

# Strings are really handy, so in this exercise you will learn how to make strings that have variables embedded in them.
# You embed variables inside a string by using specialized format sequences and then putting the variables at the end with a special
# syntax that tells Python, "Hey, this is a format string. Put these variables in there."

# As usual, just type this in even if you do not understand it and make it exactly the same.

my_name = 'Rajesh R. Pillai'
my_age = 37 # Guess
my_height = 70 # inches
my_weight = 65 #kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "Hes %d inches tall." % my_height
print "He's %d kg. heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " %(my_age, my_height,my_weight,my_age + my_height + my_weight)