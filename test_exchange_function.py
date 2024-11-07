from unittest import TestCase
from exchange import convert_currency, divide_or_square


class TestExchange(TestCase):

	def test_that_convert_currency_function_exist(self):
		convert_currency(100)
	

	def test_that_convert_currency_function_return_correct_value(self):
		self.assertEqual(convert_currency(10), 15500)
		self.assertEqual(convert_currency(20.1), 31_155)


	def test_that_convert_currency_function_return_correct_value_with_floating_value(self):
		self.assertEqual(convert_currency(20.1), 31_155)
		self.assertEqual(convert_currency(35.25), 54637.5)
	

	def test_that_convert_currency_function_raise_error_with_negative_value(self):
		self.assertRaises(ValueError, convert_currency, -12)

		
	def test_that_convert_currency_function_raise_error_with_string_value(self):
		self.assertEqual(convert_currency("williams-Gstring"), "invalid input")
		self.assertEqual(convert_currency(""), "invalid input")


class TestDivideOrSquare(TestCase):

	def test_that_divide_or_square_function_exist(self):
		divide_or_square(1)

	def test_that_divide_or_square_function_return_correct_value(self):
		self.assertEqual(divide_or_square(10), 3)



	











		

