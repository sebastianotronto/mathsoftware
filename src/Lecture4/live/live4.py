
def fun(a, b):
	print("This is function fun")
	print("I am executing!")
	print("Your parameter a:", a)
	z = a + b
	if z > 10:
		print("Your sum is large!", z)
	while z > 5:
		print("Decreasing sum:", z-1)
		z = z - 1

#fun(2, 11)
#print("..")
#fun(0, 7)

def g(x, y):
	#print("This is function g")
	return (x**2 +1)*y
	
print(g(10,2)-100)


def fibo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibo(n-1) + fibo(n-2)



print(fibo(5))
F = [fibo(x) for x in range(6)]
print(F)




