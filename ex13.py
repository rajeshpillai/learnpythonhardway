# Exercise 13: Parameters, Unpacking, Variables
# In this exercise we will cover one more input method you can use to pass variables 
# to a script (script being another name for your .py files). You know how you type 
# python ex13.py to run the ex13.py file? Well the ex13.py part of the command is 
# called an "argument." What we'll do now is write a script that also accepts arguments.

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

