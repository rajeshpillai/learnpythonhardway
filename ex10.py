# Exercise 10: What Was That?
# In Exercise 9 I threw you some new stuff, just to keep you on your toes. I showed you two ways 
# to make a string that goes across multiple lines. In the first way, I put the characters 
# \n (backslash n) between the names of the months. These two characters put a new line character 
# into the string at that point.

# This \ (backslash) character encodes difficult-to-type characters into a string. There are various 
# "escape sequences" available for different characters you might want to use. We'll try a few of these 
# sequences so you can see what I mean.

# An important escape sequence is to escape a single-quote ' or double-quote ". Imagine you have a string 
# that uses double-quotes and you want to put a double-quote inside the string. If you write 
# "I "understand" joe." then Python will get confused because it will think the " around "understand" 
# actually ends the string. You need a way to tell Python that the " inside the string isn't a real double-quote.

# To solve this problem you escape double-quotes and single-quotes so Python knows to include 
# in the string. Here's an example:

# "I am 6'2\" tall."  # escape double-quote inside string
# 'I am 6\'2" tall.'  # escape single-quote inside string
# The second way is by using triple-quotes, which is just """ and works like a string, but you also can put 
# as many lines of text as you want until you type """ again. We'll also play with these.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat




# Escape Sequences
# This all of the escape sequences Python supports. You may not use many of these, but memorize their 
# format and what they do anyway. Try them out in some strings to see if you can make them work.

# ESCAPE	WHAT IT DOES.
# \\	Backslash ()
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r ASCII	Carriage Return (CR)
# \t ASCII	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh
# Here's a tiny piece of fun code to try out:

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
# Study Drills
# Memorize all the escape sequences by putting them on flash cards.
# Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# Combine escape sequences and format strings to create a more complex format.
# Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. 
# Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?

