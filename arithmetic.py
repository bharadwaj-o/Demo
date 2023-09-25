class calculator:
	def addition(a,b):
		return (a+b)
	def subtraction(a,b):
		return(a-b)
	def multiplication(a,b):
		return(a*b)
	def division(a,b):
		return(a/b)

a=2
b=3
print("Choose the Operation:\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
c=int(input("Enter operation number:"))

if c==1:
	print("Result:",calculator.addition(a,b))
elif c==2:
	print("Result:",calculator.subtraction(a,b))
elif c==3:
	print("Result:",calculator.multiplication(a,b))
elif c==4:
	print("Result:",calculator.division(a,b))