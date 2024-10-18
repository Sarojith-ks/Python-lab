num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("which arithmetic operation do you want to perform (1/2/3/4/5/6/7)")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.floor division")
print("6.modulus")
print("7.exponentiation")
operation=int(input("select your choice: "))
if operation==1:
	result=num1+num2
	print("result:",result)
elif operation==2:
	result=num1-num2
	print("result :",result)
elif operation==3:
	result=num1*num2
	print("result :",result)
elif operation==4:
	result=num1/num2
	print("result :",result)
elif operation==5:
	result=num1//num2
	print("result :",result)
elif operation==6:
	result=num1%num2
	print("result :",result)
elif operation==7:
	result=num1**num2
	print("result :",result)
else:
	print("invalid entry")




