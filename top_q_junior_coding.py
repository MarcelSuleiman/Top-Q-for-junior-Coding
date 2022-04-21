'''
Q: Write a function that produces the Fibonacci sequence.
'''

def fibo(n: int) -> list:

	if n == 0:
		return []

	elif n == 1:
		return [0,]

	elif n > 1:

		a = 0
		b = 1

		seq = [0,1]

		for i in range(n-2):
			temp = b

			b = a + b
			a = temp

			seq.append(b)

		return seq

n = 1
print(fibo(n))

'''
Q: How to translate a string containing a binary code (1 and 0) into a number (integer)? Write a function to do this.
'''

def string_binary_code_2_num(string:str) -> int:
	return int(string, 2)

def string_binary_code_2_num_no2(string:str) -> int:
	string_list = list(string)
	length = len(string_list)-1

	result = 0

	for element in string_list:
		result += int(element) * (2**length)

		length -= 1

	return result


string = '1010101011101101010101010100101010101000100110111000101010111'
print(string_binary_code_2_num(string))
print(string_binary_code_2_num_no2(string))

'''
Q: How to check that tuple A contains all elements of tuple B. Do both tuples contain unique values? Write a function to do this.
'''

def check_contains(a:tuple, b:tuple) -> str:
	count = 0

	if a == b:
		return 'Tuple "A" contains all elements of tuple "B".'

	else:
		for element in a:
			if element in b:
				count += 1

		if count == 0:
			return 'Both tuples contain unique values.'

		else:
			return f'Tuple "A" contains {count} elements of tuple "B".'


# a = (1,2,3)
a = ('a','b')
b = (1,2,3,4)
print(check_contains(a, b))

'''
Q: What is the output of the following code?
'''

def f():
     x = 15
     print(x)
x = 12
f()

# output is 15

'''
Q: How to convert a string to a number that consists of letters ASCII code. Example: 'abcd' -> 979899100. Write a function to do this.
'''

def convert_string_2_num(string:str) -> int:
	result = ''
	for char in string:
		result += str(ord(char))

	result = int(result)
	return result

string = 'abcd'
print(convert_string_2_num(string))

'''
Q: How to remove empty lines from a list of lines (with a length of 0). Write a function to do this.
'''

def remove_empty_lines(lines:list) -> list:
	count = lines.count('')
	for i in range(count):
		lines.remove('')

	return lines

lines = ['first line','','third line','','','last line']
print(remove_empty_lines(lines))

'''
Q: Write a function that counts all distinct pairs with a difference equal to k.
'''

def counts_all_distinct(pairs_list:list, k:int) -> int:
	# results = []
	result = 0

	for element in pairs_list:
		if abs(element[0] - element[1]) == k:
			# results.append(element[0]+element[1])
			result += element[0]+element[1]

	return result

pairs = [[5,3],[7,6],[10,8],[2,2],[7,5]]
print(counts_all_distinct(pairs, 2))


'''
Q: Write a function that returns a string of numbers from 0 to 100, "0123456789101112...".
'''

def return_string_of_nums(start:int, stop:int) -> str:
	stop += 1
	data = range(start, stop)

	result = ''
	for element in data:
		result += str(element)

	return result

def return_string_of_nums_no2(start:int, stop:int) -> str:
	result = ''.join(map(str, range(start, stop+1)))
	return result

start = 0
stop = 100
print(return_string_of_nums(start, stop))
print(return_string_of_nums_no2(start, stop))

'''
Q: Write a function that makes a list with unique items from a list with duplicate items. Example: [1, 1, 2, 3, 3] -> [1, 2, 3].
'''

def make_a_list_of_unique_items(data:list) -> list:
	return list(set(data))

def make_a_list_of_unique_items_no2(data:list) -> list:

	new_data = []
	for element in data:
		if element not in new_data:
			new_data.append(element)

	return new_data

data = [8,1,1,2,3,3,1,4,56,25,25,66,33,33,22,21]
print(make_a_list_of_unique_items(data))
print(make_a_list_of_unique_items_no2(data))

'''
Q: Make a list of prime numbers from the range (1, 100) using Python.
'''

def make_a_list_of_prime_numbers(start:int, stop: int) -> list:

	list_of_prime_numbers = []

	for i in range(start, stop):
		if i > 1:
			flag = True
			for j in range(2, int(i**1/2)+1):
				if (i % j) == 0:
					flag = False
					break

			if flag == True:
				# number is prime number
				list_of_prime_numbers.append(i)

	return list_of_prime_numbers

start = 1
stop = 100
print(make_a_list_of_prime_numbers(start, stop))

'''
Q: Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers that are multiples of both three and five print “FizzBuzz”.
'''

def program(start:int, stop:int) -> None:

	for i in range(start, stop+1):
		if i % 3 == 0 and i % 5 == 0:
			print('FizzBuzz')

		elif i % 3 == 0:
			print('Fizz')

		elif i % 5 == 0:
			print('Buzz')

		else:
			print(i)

start = 1
stop = 20
program(start, stop)
