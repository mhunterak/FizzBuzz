for i in range(1,101):
	s=''
	if i%3 == 0:
		s+="Fizz"
	if i%5 == 0:
		s+="Buzz"
	if 0 != i%3 and i%5:
		s=i
	print s
