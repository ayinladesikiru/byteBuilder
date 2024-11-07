'''
prompt for password
store in variable password
get the length of the password
display password in astericks
'''

password = input("Enter password: ")

password_count = len(password)

password_astericks = '*' * password_count
print(password_astericks)


