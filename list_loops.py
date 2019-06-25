def second_minimum(number):
	number
	i = 0
	num=1
	if len(number) < 0:
		print 0
	else:
		while len(number) >= 0:
			i = i + num
			num = num + 1
			print number[num]          

print(second_minimum([70, 50, 20, 23, 40]))
print(second_minimum([70, 50, 10, 2, 40]))
