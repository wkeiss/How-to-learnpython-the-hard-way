#用来看break是个啥
list = []
for i in range(5):
	while i > 0:
		print"Now i is %d." % i
		list.append(i)
		i = i + 1
		break
#break 放在哪里，就能让while循环在哪里停止，觉得这可以结合print,用来调试代码，看看所写的循环程序是不是符合自己的预期。
	
#试试运用with as statement 来替换单独使用open，read命令来操作文件
from sys import argv
script, filename = argv		
with open(filename) as new_count: 
	print new_count.read()
	 
	
#原来使用test.txt时需先import.
#import后不能直接使用test.txt,而应该使用filename这个形参。
#with as statement 让文件操作的代码变得更简洁了

		

		
	
