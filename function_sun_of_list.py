def sum_of_list():
	print('0=結束輸入')
	numbers = []

	while True:
		x = int(input('請輸入欲加總的數字：'))
		if x == 0:
			break
		else:
			numbers.append(x)

	# s = sum(numbers)
	# return s
	return sum(numbers)

print(sum_of_list())