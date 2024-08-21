'''
prompt user for radius
store the value in variable name radius
create a variable name pi
store the value 3.142 in variable pie
calculate area of the circle using the formular
store the result in a variable name area
display the result
'''

radius = int(input("Enter radius: "))
name = input("Enter your name: ")
PI = 3.142
area = PI * (radius ** 2)

print("The area of circle with", radius, "is", round(area, 2))
print("Thank you", name, "for using our program")
