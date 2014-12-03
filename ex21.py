# Exercise 21: Functions Can Return Something
# You have been using the = character to name variables and set them to numbers 
# or strings. We're now going to blow your mind again by showing you how to use = 
# and a new Python word return to set variables to be a value from a function. 
# There will be one thing to pay close attention to, but first type this in:

def add(a, b):
	print "ADDING %d + %d" %(a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

