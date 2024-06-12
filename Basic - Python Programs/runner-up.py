n=int(input("How many numbers?"))

def fun(n):
	for i in range(n):
		m = int(input("Enter number: "))
		yield m

b=list(fun(n))
b.sort(reverse=True)
print(b[1])