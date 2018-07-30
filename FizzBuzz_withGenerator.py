#FizzBuzz with generators
def mygenerator(maxValue):
	for i in xrange(1,maxValue+1):
		if 0 == i%3 and i%5:
			yield "FizzBuzz"
		elif 0 == i%3:
			yield "Fizz"
		if i%5 == 0:
			yield "Buzz"
		if 0 != i%3 and i%5:
			yield i

#FizzBuzz with a list comprehension
l=[x for x in mygenerator(100)]
