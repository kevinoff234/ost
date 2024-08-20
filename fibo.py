def fibonacci(n):
	if n is 0 or n is 1:
		return n;
	else:
		return fibonacci(n-1)+fibonacci(n-2)

#main
num = int(input("enter a number"))
fib = fibonacci(num)
print("fibonacci at nth element"+fib)



