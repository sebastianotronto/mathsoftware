print(2+2)

x = input("Input something: ")
print("Your input was:", x, "of type", type(x))

x_number = int(x)
print("Converted to a number:", x_number, "of type", type(x_number))

if x_number > 10:
	print("Your number was large!")
	print("It was larger than 10")
	z = x_number-10
	print("This is a smaller number:", z)
else:
	print("Your number was small")
	
print("Bye")
