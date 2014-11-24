# Exercise 12: Prompting People
# When you typed raw_input() you were typing the ( and ) characters, which are 
# parenthesis characters. This is similar to when you used them to do a format 
# with extra variables, as in "%s %s" % (x, y). For raw_input you can also put 
# in a prompt to show to a person so he knows what to type. Put a string that 
# you want for the prompt inside the () so that it looks like this:

# y = raw_input("Name? ")
# This prompts the user with "Name?" and puts the result into the variable y. 
# This is how you ask someone a question and get the answer.

# This means we can completely rewrite our previous exercise using just raw_input to do all the prompting

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % ( age, height, weight)


