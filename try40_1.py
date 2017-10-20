# put lyrics to a variable,and send it to the module.
class Song(object):

	def __init__(self, lyrics):
		self.lyrics =lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

variable = ["class like a mini module",
				"we can import it too",
				"a module like a dictonary",
				"we can use the keyword to use it"]			
class1 = Song(variable)
				
class1.sing_me_a_song()