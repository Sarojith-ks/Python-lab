def add(n1,n2):
	return n1+n2
def subtract(n1,n2):
	return n1-n2
def multiply(n1,n2):
	return n1*n2
def divide(n1,n2):
	return n1/n2
def power(n1,n2):
	return n1**n2
def calculator(n1,operator,n2):
	if operator=="+":
		return add(n1,n2)
	if operator=="-":
		return subtract(n1,n2)
	if operator=="*":
		return multiply(n1,n2)
	if operator=="/":
		return divide(n1,n2)
	if operator=="**":
		return power(n1,n2)
	else:
		print("invalid!")
		
n1=int(input("enter first number :"))
n2=int(input("enter second number :"))
operator=input("\n enter any operator :\n+\n-\n*\n/\n**\n")
result=calculator(n1,operator,n2)
print("result=",result)
