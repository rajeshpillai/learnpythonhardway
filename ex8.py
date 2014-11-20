# Exercise 8: Printing, Printing
# We will now see how to do a more complicated formatting of a string. This code looks complex, 
# but if you do your comments above each line and break each thing down to its parts, you'll understand it.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)