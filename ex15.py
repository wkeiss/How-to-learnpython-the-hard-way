#import the module named "argv" 
from sys import argv
#pick out the two argument "script" and "filename" from the package "argv"(from Zed)
script, filename = argv
#use the function "open" to return a data,which is assign the variable "txt" as a value 
txt = open(filename)
#use the format string "%r" ,it will returns the sentence"Here's your file filename."
print"Here's your file %r:" % filename
#use to function "read" to make python to print the content of txt.
print txt.read()
#present the sentence"Type the filename again:"
print"Type the filename again:"
#to let the user input something,which willed be assigned to variable "file_name"
file_again = raw_input(">")
#use the function "open",which will return a value to the variable"txt_again".
txt_again = open(file_again)
#print the content of txt_again.
print txt_again.read()

txt.close()
txt_again.close()