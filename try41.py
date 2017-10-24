# Animal is basic class
class Animal(object):

	def __init__(self, name):
		self.name = name
		
	def what(self):
		print "This is %s." % self.name
		
a = Animal('tiger')
a.what()

class Fish(object):

	def __init__(self, name):
		self.name = name
		
	def what(self):
		print "This is %s." % self.name
		
b = Fish('tiger')
b.what()

# Animal is an object here.
class Dog(Animal):

	def __init__(self, name):
		## self have_a name some kind
		self.name = name

c = Dog('tiger')
c.what()

