#people are always trouble in choosing,if there is a programmer that can help people choose,wow,so great!

print"If you are trouble in make a choice between A and B."

print"you can input #1 and #2 to see what will happen, and then you wil make a choice."

input = raw_input(">")

if input == "1":#remember that "=" links string
	print"now you cannot choose B."
	print"When you acknowledge that you cannot choose B,how did you feel?"
	print"Did you know how to choose?"
	input1 = raw_input("Yes/No?")
	if input1 == "Yes":
		print"Well done!"
	
	elif input1 == "No":
		print"Try to redefine the problem,sometimes problem emerges from your mind ,not the obejects themselves."

elif input == "2":
	print"now you cannot choose A."
	print"When you acknowledge that you cannot choose A,how did you feel?"
	print"Did you know how to choose?"
	input2 = raw_input("Yes/No?")
	if input2 == "Yes":
		print"Well done!"
	
	elif input2 == "No":
		print"Try to redefine the problem,sometimes problem emerges from your mind ,not the obejects themselves."
	

else:
	print"Try to jump out the situation of choosing one from two , figure out what's your real problem and sovle the problem diretly."
	
#small reflection:
#1.if 后应加上一个逻辑判断式。
#2.if下在嵌套if语句时，注意缩进。
#3.使用raw_input输入的指的类型都是string。
#4.这次将我阅读的《改变》一书的第二序改变，重新框定问题，突破二选一困境用代码表现出来，这样的将喜欢的事情结合起来的感觉很棒！
#5.代码完成后的第一步是在解决#1，#2和#3的问题，但是离好的代码风格——代码有输入时，应将所有可能输入的情况都考虑在内，还有些距离。比如用户在输入input1或input2的值时，可能会输入小写的yes 或no,这是可以提醒用户输入“Yes“ 或"No".
	
