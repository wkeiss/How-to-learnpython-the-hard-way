def add(a,b):
	print"ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print"SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print"MUTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print"DIVIDING %d / %d" % (a, b)
	return a / b
	
print"Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print"Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
#print"Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print"That becomes: ", what, "Can you do it by hand?"

#print"I am going to use nomal way to figure it out:"
#what =( height -iq / 2 * weight ) + age
#print "what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
 #= ( height -iq / 2 * weight ) + age 
# = %d " % what

#print"Yeah! I made it!!"

#try to use the functions of this exercise to figure some equotation out!eg.( 45/9 + 397 ) /100 * 42

a = multiply(divide(add(divide(45, 9), 397), 100), 42)
b = ( 45/9 + 397 ) /100 * 42
print"a = b?right?"
print "a = %d" % a, "b = %d" % b






