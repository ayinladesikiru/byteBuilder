number = int(input("Enter a number or 0 to stop: "))
numbers = []

while number != 0:
	numbers.append(number)
	number = int(input("Enter a number or 0 to stop: "))

print(numbers)

total = 0
count = 0
for n in numbers:
	total += n
	count += 1

average = total / count

average = sum(numbers) / len(numbers)

print(average)
	





	