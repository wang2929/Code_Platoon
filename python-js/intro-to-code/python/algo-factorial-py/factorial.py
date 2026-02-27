def factorial(num):
	# your code here
	val = 1
	for i in range(1, num+1, 1):
		val = val * i
	return val