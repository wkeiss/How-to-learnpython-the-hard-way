ten_things = "Apples Oranges Crows Telephone Light Sugar"

print"Wait there are not 10 things in that list.Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()#assgin the last one item of the list "more_stuff" to "next_one".
	print"Adding: ", next_one
	stuff.append(next_one)
	print"There are %d items now." % len(stuff)
	
print"There we go: ", stuff

print"Let's do some things with stuff."

print stuff[1]#vist the no.2 item of the list
print stuff[-1] #whoa! fancy
print stuff.pop()#show the last one item of the list
print' '.join(stuff) #what?coll!#=print stuff
print'#'.join(stuff[3:5])#super stellar!

