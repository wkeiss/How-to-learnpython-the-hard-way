def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.poop(0)#"poop' should be 'pop'
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1#need the ")"
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000#"\" should be"/"
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)#"start-point" need to be "start_point"

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont#we need add ")",and change the "start_pont" to "start-point"


sentence = "All god\tthings come to those who weight."#"All good things come to those who wait."

words = ex25.break_words(sentence)#word = break_words(sentence)
sorted_words = ex25.sort_words(words)#sorted_wrods = sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)#print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)#sorted_words = sort_sentence(sentence)
prin sorted_words#print sorted_words

print_irst_and_last(sentence)#print_first_and_last(sentence)

   print_first_a_last_sorted(senence)#cancel the "tab"，print_first_and_last_sorted(sentence)
   
   # how did I find out these mistakes?
   # first,I read the code starting with the first line,and I try to figure out what the code are used for.At the same time,I would keep an eye on the spling mistakes.Sometimes,there was no mistakes both in speling and grammer,I would chage the code to the code in ex24.py and ex25.py."
   #Second,I would run the code I have checked and refined,then found more mistakes that I missed through Pyhton and hacked them untli there is no mistakes.
   
