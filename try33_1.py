numbers = []

def new_function(j):
	j = int(j)
	i = 0
	while i < j:
		print"At the top i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print"Numbers now: ", numbers
		print"At the bottom i is %d" % i
		
new_function(6)
		
print"The numbers:"

for num in numbers:
	print num
	
#atualy,I almostly build the function intuitively,and I depend on python to refine my code,like use function "int" to change the type of "j",and remove the "i = 0" from the line1 to the line5.Surprisingly,I got the result the same as ex33.py!
	