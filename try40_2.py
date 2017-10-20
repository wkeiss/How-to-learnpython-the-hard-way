# use class for other things
class Article(object):
	
	def __init__(self, sentences):
		self.sentences = sentences
		
	def show_me_sentence(self):
		for line in self.sentences:
			print line
			
			
a = ["How nice this morning!The air is fresh,the bird is singing."]
b = ["I got up at 6:35,and opened the computer to finish this task."]
c = ["Now,I am in good mood.:)"]

morning = Article(a)
get_up = Article(b)
mood = Article(c)

morning.show_me_sentence()

get_up.show_me_sentence()

mood.show_me_sentence()