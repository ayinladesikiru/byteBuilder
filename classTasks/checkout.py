from datetime import datetime


product_list = []
price_list = []
quantity_list = []

customer_name = input("what is the customer name: ")
product_name = input("what did the customer buy: ")
quantity = int(input("How many pieces: "))
unit_price = float(input("How much per unit: "))

product_list.append(product_name)
price_list.append(unit_price)
quantity_list.append(quantity)

customer_response = input("Add more items: ")

while customer_response.lower() == "yes":
	product_name = input("what did the customer buy: ")
	product_list.append(product_name)
	quantity = int(input("How many pieces: "))
	quantity_list.append(quantity)
	unit_price = float(input("How much per unit: "))
	price_list.append(unit_price)
	
	customer_response = input("Add more items: ")


cashier_name = input("what is the cashier's name: ")
sub_total = 0

for price, quantity in zip(price_list, quantity_list):
	sub_total += (price * quantity)
	
discount = float(input("How much discount will the customer get: "))
VAT = 17.50
vat_charge = (VAT / 100) * sub_total
bill_after_discount = sub_total - discount
bill = bill_after_discount + vat_charge

date = datetime.now()

invoice = f"""
	SEMICOLON STORE
	MAIN BRANCH
	LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
	TEL: 09091967419
	DATE: {date}
	Cashier: {cashier_name}
	Customer Name: {customer_name}
======================================================================================================
	ITEM	QTY	PRICE	TOTAL(NGN)
------------------------------------------------------------------------------------------------------
						
	for index in range(len(product_list)):
		{print(product_list[index])}													


-------------------------------------------------------------------------------------------------------
					Sub Total:	{sub_total}	
					Discount:	{discount}
					VAT @ 17.50%:	{vat_charge}
=======================================================================================================
					BILL TOTAL: 	{bill}
=======================================================================================================
		THIS IS NOT YOUR RECIEPT, KINDLY PAY
=======================================================================================================
"""

print(invoice)

payment_amount = float(input("How much did the customer give you? "))
while payment_amount < bill:
	payment_amount = float(input("How much did the customer give you? "))

balance = payment_amount - bill

receipt = f"""
	SEMICOLON STORE
	MAIN BRANCH
	LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
	TEL: 09091967419
	DATE: {date}
	Cashier: 
	Customer Name: {customer_name}
======================================================================================================
	ITEM	QTY	PRICE	TOTAL(NGN)
------------------------------------------------------------------------------------------------------
						
																


-------------------------------------------------------------------------------------------------------
					Sub Total:	{sub_total}	
					Discount:	{discount}
					VAT @ 17.50%:	{vat_charge}
=======================================================================================================
					BILL TOTAL: 	{bill}
					Amount Paid:	{payment_amount}
					Balance: 	{balance}
=======================================================================================================
		THIS IS NOT YOUR RECIEPT, KINDLY PAY
=======================================================================================================
"""
print(receipt)


