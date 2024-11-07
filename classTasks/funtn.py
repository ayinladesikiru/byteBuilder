def get_maximum(n1, n2, n3=7):
	largest = n1
	if n2 > n1:
		largest = n2
	elif n3 > largest:
		largest = n3
		
	return largest

print(get_maximum(2, 3, 7))
