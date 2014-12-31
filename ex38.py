# Exercise 38: Doing Things to Lists
# You have learned about lists. When you learned about while-loops you "appended" numbers to the end of a list and printed them out. There were also Study Drills where you were supposed to find all the other things you can do to lists in the Python documentation. That was a while back, so review those topics if you do not know what I'm talking about.

# Found it? Remember it? Good. When you did this you had a list, and you "called" the function append on it. However, you may not really understand what's going on so let's see what we can do to lists.

# When you write mystuff.append('hello') you are actually setting off a chain of events inside Python to cause something to happen to the mystuff list. Here's how it works:

# Python sees you mentioned mystuff and looks up that variable. It might have to look backward to see if you created with =, if it is a function argument, or if it's a global variable. Either way it has to find the mystuff first.
# Once it finds mystuff it reads the . (period) operator and starts to look at variables that are a part of mystuff. Since mystuff is a list, it knows that mystuff has a bunch of functions.
# It then hits append and compares the name to all the names that mystuff says it owns. If append is in there (it is) then Python grabs that to use.
# Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.
# That extra argument is ... mystuff! I know, weird, right? But that's how Python works so it's best to just remember it and assume that's the result. What happens, at the end of all this, is a function call that looks like: append(mystuff, 'hello') instead of what you read which is mystuff.append('hello').

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!


