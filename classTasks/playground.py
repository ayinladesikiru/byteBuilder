score = int(input("Enter score: "))


if score > 100:
	print("Invalid score")
elif score >= 75 and score <= 100:
	print("Your grade is A")
elif score >= 65 and score < 75:
	print("Your grade is B")
elif score >= 50 and score <= 64:
	print("Your grade is C")
elif score >= 40 and score <= 49:
	print("your grade is D")

else:
	print("failed")


