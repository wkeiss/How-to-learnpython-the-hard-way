from sys import exit

def gold_room():
	print"This room is full of gold. How much do you take?"
	
	choice = raw_input(">")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	if  how_much < 50:
		print"Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print"There is a bear here."
	print"The bear has a bunch of honey."
	print"The fat bear is in front of another door."
	print"How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input(">")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "Taunt bear" and not bear_moved:
			print"The bear has moved from the door. You can go through in now."
			bear_moved = True
		elif choice == "Taunt bear" and bear_moved:
			deaf("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print"I got no idea what that means."
			
def cthulhu_room():
	print"Here you see the great evil Cthulhu."
	print"He, it, whatever stares at you and you go insane."
	print"Do you feel for your life or eat your head?"
	
	choice = raw_input('>')
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
	
def dead(why):
	print why, "Good job!"
	exit(0)#exit() means stoping running the program
	
def start():
	print"You are in a dark room."
	print"There is a door to your right and left."
	print"Which one do you take?"
	
	choice = raw_input('>')
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()
			
		
	
#感觉这次的代码信息量好大啊！我有如此多的困惑呢。1.为什么不先建立start()和dead()这两个在前面的代码就已经先用到的函数，而放到最后？2.在建构bear_room()这个函数中，为什么要用while true来建立无限循环？这岂不是违背简洁的原则吗？