#from sys import the module argv
from sys import argv

#pick out two argument from the 'package' argv
script, input_file = argv

#line 6-13 are used to build new function
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()

#assign the value which use statement 'open' to the variable	
current_file = open(input_file)

#show the sentence under the double_qoute
print"First let's print the whole file:\n"

#use the function print_all(f), and f = current_file
print_all(current_file)

#show the sentence under the double_qoute
print"Now let's rewind, kind of like a tape."

#use the function rewind(f),and f = current file
rewind(current_file)

#show the sentence under the double_qoute
print "Let's print three lines:"

#assign the new value to the variable
current_line = 1
#use the fuction to print_a_line to use the current line and its content.
print_a_line(current_line, current_file)

#assign the new value to the variable
current_line = current_line + 1
#use the fuction to print_a_line to use the current line and its content. 
print_a_line(current_line, current_file)

#assign the new value to the variable
current_line = current_line + 1
#use the fuction to print_a_line to use the current line and its content.
print_a_line(current_line, current_file)