letter = "\nA \nB \nC \nD\n..."
print "What are English letters?%s" %letter

Answer = "\nshe said:\'I forget something.'"
print "I didn't understood what she said.%s" %Answer
print "I didn't understood what she said.%r" %Answer
#%r means let python show you the code,while %s make python show you what the coder want you know.
#or we can say that: '%r' show me the language of computer,'%s' show me the language of man.

apple = 15 #$
orange = 20 #$
coffe = 19 #$/cup
bread = 25 #$
addition = apple + orange + coffe + bread

print"I am going to check my bill.\n\t*apple\n\t*orange\n\t*coffe\n\t*bread "
print"let me make a additon for them.%s" %addition 
print"uh! I need to pay", addition ,"$!"

#We can also do like this:
print"""
I am going to check my bill.
\t*apple
\t*orange
\t*coffe
\t*bread
let me make a addition for them.%s
"""% addition



