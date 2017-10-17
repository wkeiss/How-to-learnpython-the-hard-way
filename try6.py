#give string "There are 10 types of people." to the variable "x"
x = "There are %d types of people." % 10
#give string "binary" to the valuable "binary"
binary = "binary"
#give the string "don't" to the variable "do_not" as a values.
do_not = "don't"
#give the string "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)
#show the values of x
print x
#show the values of y
print y 
#show the string "I said :'There are 10 types of people."
print "I said: %r." % x
#show the string "I also said:'Those who know binary and those who don't.'"
print "I also said: '%s'." % y
#give the string "False" to the variable "hilarious"
hilarious = False
#give the string"" to the variable "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"
#show the string"Isn't that joke so funny?!False"
print joke_evaluation % hilarious
#give the string"This is the left side of..." to the variable "w"
w = "This is the left side of..."
#give the string"a string with a right side."to "e"
e = "a string with a right side."
#show w and e together.
print w + e