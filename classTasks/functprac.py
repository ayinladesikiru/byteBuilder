def get_multiplication_table(number):
	for i in range(1, 13):
		for j in range(1, number+1):
			print(f"{i:>2} x {j:<2} = {i * j:<4}", end='')
		print()



get_multiplication_table(20)