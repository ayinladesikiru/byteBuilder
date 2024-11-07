balance = 0

x = 0

menu = """
Enter option 1 to deposit 
or 2 to withdraw
3 to check balance
0 to end: """

user_input = input(menu)

while user_input != '0':
	if user_input == '1':
		amount = float(input("Enter amount: "))
		balance += amount
	elif user_input == '2':
		amount = float(input("Enter amount: "))
		if balance < amount:
			print("Insufficient fund")
		else:
			balance -= amount
	elif user_input == '3':
		print("your balance is ", balance)

	user_input = input(menu)

		
def get_orange():
	global x
	return 1
	
