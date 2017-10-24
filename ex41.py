## Animal is_a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is_a Animal
class Dog(Animal):

	def __init__(self, name):
		## self have_a name some kind
		self.name = name
		
## Cat is_a Animal.
class Cat(Animal):

	def __init__(self, name):
		## self have_a name of some kind
		self.name = name
		
class Person(object):

	def __init__(self, name):
		## self have_a name of some kind
		self.name = name
		
		## Person has_a pet of some kind
		self.pet = None
		
## Employee is_a Person
class Employee(Person):

	def __init__(self, name, salary):
		##?? hmm what is this stange magic?
		super(Employee, self).__init__(name)
		## self has_a salary of som kind
		self.salary = salary
		
## Fish is_a object.
class Fish(object):
	pass
	
## Salmon is_a Fish.
class Salmon(Fish):
	pass
	
## Halibut is_a Fish.
class Halibut(Fish):
	pass
	
## rover is_a dog
rover = Dog("Rover")

## satan is_a Cat.
satan = Cat("Satan")

## mary is_a Person.
mary = Person("Mary")

## mary has_a pet of some kind.
mary.pet = satan

## frank is a Employee.
frank = Employee("Frank", 120000)

## frak has_a pet of some kind.
frank.pet = rover

## flipper is_a Fish.
flipper = Fish()

## crouse is_a Salmon.
crouse = Salmon()

## harry is_a Halibut.
harry = Halibut()



