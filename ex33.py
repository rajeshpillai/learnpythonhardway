# Exercise 33: While Loops
# Now to totally blow your mind with a new loop, the while-loop. A while-loop will keep executing the code block under it as long as a boolean expression is True.

# Wait, you have been keeping up with the terminology, right? That if we write a line and end it with a : (colon) then that tells Python to start a new block of code? Then we indent and that's the new code. This is all about structuring your programs so that Python knows what you mean. If you do not get that idea then go back and do some more work with if-statements, functions, and the for-loop until you get it.

# Later on we'll have some exercises that will train your brain to read these structures, similar to how we burned boolean expressions into your brain.

# Back to while-loops. What they do is simply do a test like an if-statement, but instead of running the code block once, they jump back to the "top" where the while is, and repeat. A while-loop runs until the expression is False.

# Here's the problem with while-loops: Sometimes they do not stop. This is great if your intention is to just keep looping until the end of the universe. Otherwise you almost always want your loops to end eventually.

# To avoid these problems, there are some rules to follow:

# Make sure that you use while-loops sparingly. Usually a for-loop is better.
# Review your while statements and make sure that the boolean test will become False at some point.
# When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.
# In this exercise, you will learn the while-loop while doing these three checks:

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Number now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

	