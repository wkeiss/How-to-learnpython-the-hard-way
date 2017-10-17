def upstairs():
	print"""There is a table here!
There are a plenty of delicious foods on the table,such as bread, hot milk, meat, fruits, juice, icecream and so on!
Do you eat or not?
"""
	
	eat_choice = raw_input(" please input 'eat' or 'not'!  ")
	
	if "eat" in eat_choice:
		print"Now you can enjoy your food."
		print"Unfortunately, an old lady show up when you are enjoying the food."
		print"""an old lady ask you to pay for the dinner by doing one of the two things that she give you to choose.
now you must choose A or B first,which represent the two things.
Which one would you choose?
"""
		ab_choice = raw_input("please input 'A' or 'B'!  ")
		
		if "A" in ab_choice or "a" in ab_choice:
			print"you need to be companied with the old lady for 24h."
		elif "B" in ab_choice or "b" in ab_choice:
			print"you need to tell 3 stories about you to the old lady."
		else:
			print"Please input following the instruction in the prompt!Game over!"
			exit(0)
			
	elif "not" in eat_choice:
		print"You are so hungary, why not??"
		print"You're so hard that I don't no how to decide your life!Goodbye and goodluck!"
	else:
		print"Please input following the instruction in the prompt!Game over!"
		exit(0)
			
			
def right_door():
	print"You open the door.A big beautiful garden is shown to you!"
	print"You are shocked, and you cannot help going around the garden."
	
def left_door():
	print"You open the door.A large library is shown to you!"
	print"There are many many many books.Wow!"
	print"You love this place so much!"
	
def start():
	print"""You got lost, suddenly a castle lying front you.
you are very hungary and have no eat food for one day.
so you come into the castle,hoping for some food.
There are two doors,one is in your left,the other is in your right.and there is a stair to upstairs.
Which door will you open? or you go upstairs?
"""
	start_choice = raw_input("Please input 'right', 'left' and 'upstairs'")
	
	if "right" in start_choice:
		right_door()
	elif "left" in start_choice:
		left_door()
	elif"upstairs" in start_choice:
		upstairs()
	else:
		print"Please input following the instruction in the prompt!Game over!"
		exit(0)

			
start()
		




	
	
	
			
		
	