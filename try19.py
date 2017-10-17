#line2-6 are used to create a new function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print"You have %d cheeses!" % cheese_count
	print"You have %d boxes of crackers!" % boxes_of_crackers
    print"Man that's enough for a party!"
    print"Get a blanket.\n"
	
#show the sentence under the double_qoute	
print"We can just give the function numbers directly:"
#use the function cheese_and_crackers
cheese_and_crackers(20, 30)

#show the sentence under the double_qoute
print"OR, we can use variables from our script:"
#assign the value 10 to the variable "amount_of_cheese"
amount_of_cheese = 10
#assign the value 50 to the variable "amount_of_crakers".
amount_of_crackers = 50

#use the function "cheese_and_crackers"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#show the sentence under the double_qoute
print"We can even do math inside too:"
#use the function "cheese_and_crackers"
cheese_and_crackers(10 + 20, 5 + 6)

#show the sentence under the double_qoute
print"And we can combine the two,variables and math:"
#use the funtion "cheese_and_crackers"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
