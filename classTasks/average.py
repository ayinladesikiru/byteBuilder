'''
prompt for first number
store in a variable number1
prompt for second number
store in a variable number2
prompt for third number 
store in a variable3
calculate the sum and store in a variable name total
calculate the average and store in a variable name average
'''

number1, number2, number3 = eval(input("Enter the three number: "))

average = sum([number1, number2, number3]) / 3

print("The average of", number1, number2, number3, "is", average)