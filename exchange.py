def convert_currency(dollar_amount: float)->int:
	RATE = 1550
	if type(dollar_amount) not in [int, float]:
		return "invalid input"
	if dollar_amount < 0:
		raise ValueError("Invalid amount")
	return round(dollar_amount * RATE, 2)


def divide_or_square(number):
	pass