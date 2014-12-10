# Exercise 32: Loops and Lists
# You should now be able to do some programs that are much more interesting. 
# If you have been keeping up, you should realize that now you can combine 
# all the other things you have learned with if-statements and boolean expressions 
# to make your programs do smart things.

# However, programs also need to do repetitive things very quickly. We are going 
# to use a for-loop in this exercise to build and print various lists. When you 
# do the exercise, you will start to figure out what they are. I won't tell you 
# right now. You have to figure it out.

# Before you can use a for-loop, you need a way to store the results of loops 
# somewhere. The best way to do this is with lists. Lists are exactly what their 
# name says: a container of things that are organized in order from first to last. 
# It's not complicated; you just have to learn a new syntax. First, there's how you make lists:

# hairs = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

# You start the list with the [ (left bracket) which "opens" the list. Then you put each item you want in the list separated by commas, similar to function arguments. Lastly, end the list with a ] (right bracket) to indicate that it's over. Python then takes this list and all its contents and assigns them to the variable.

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we cn also build lists, first start with an empty oranges
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

	