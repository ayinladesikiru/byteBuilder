menu = """1 -> deposit
2 -> withdraw
3 -> balance
0 -> to quit: """

balance = 0
option = input(menu)

while option != 0:
	if option == '1':
		deposit_amount = float(input("Enter the amount you want to deposit: "))
		balance += deposit_amount
		option = input(menu)
	elif option == '2':
		withdraw_amount = float(input("Enter the amount you want to withdraw: "))
		if withdraw_amount <= balance:
			balance -= withdraw_amount
			option = input(menu)
			break
		else:
			print("Insufficient funds")
			option = input(menu)
	elif option == '3':
		print("Your balance is ", balance)
		option = input(menu)
		break
	
print("Thank you for banking with us")




	