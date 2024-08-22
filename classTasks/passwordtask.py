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


sentence = "The up and down arrow keys navigate backwards and forwards through the current interactive session’s snippets. Pressing Enter re-executes the snippet that’s displayed. Let’s set
grade to 99"

print(sentence)