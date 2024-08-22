menu = """
1. phone book
2. messages
3. Chat
4. Call Register
5. Tones :
"""

option = int(input(menu))

if option == 1:
	phone_book_menu = """
	1. Search
	2. Erase : 
	"""
	phonebook_option = int(input(phone_book_menu))
	if phonebook_option == 1:
		print("Search")
	elif phonebook_option == 2:
		print("Erase")

	