# Exercise 11: Asking Questions
# Now it is time to pick up the pace. You are doing a lot of printing to get you familiar 
# with typing simple things, but those simple things are fairly boring. What we want to do now
# is get data into your programs. This is a little tricky because you have to learn to do two 
# things that may not make sense right away but trust me and do it anyway. It will make sense in a few exercises.

# Most of what software does is the following:

# Take some kind of input from a person.
# Change it.
# Print out something to show how it changed.
# So far you have been printing strings, but you haven't been able to get any input from a person. 
# You may not even know what "input" means, but type this code in anyway and make it exactly the 
# same. In the next exercise we'll do more to explain input.


print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)