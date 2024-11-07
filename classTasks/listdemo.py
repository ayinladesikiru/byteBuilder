board = [0] * 9

for i, v in enumerate(board):
	if i != 0 and i % 3 == 0:
		print()

	print(f'{v:^3}', end='')
	
	