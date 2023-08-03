# map 1

def square_numbers(numbers):
    squared_list = list(map(lambda x: x**2, numbers))
    return squared_list

numbers_list = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers_list)
print(squared_numbers)

# map 2

def convert_to_uppercase(strings_list):
    uppercase_list = list(map(str.upper, strings_list))
    return uppercase_list


input_list = ["riyaz", "work", "fusemachines"]
uppercase_strings = convert_to_uppercase(input_list)
print(uppercase_strings)


# filter 1

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime_numbers(numbers_list):
    prime_numbers = list(filter(is_prime, numbers_list))
    return prime_numbers


input_list = [21, 42, 53, 34, 95, 56, 78, 81, 19, 1]
prime_numbers = filter_prime_numbers(input_list)
print(prime_numbers)




# reduce 2

from functools import reduce

def concatenate_strings(strings_list):
    concatenated_string = reduce(lambda x, y: x + y, strings_list)
    return concatenated_string


input_list = ["You'll", " ", "Never", " ", "Walk", " ", "Alone"]
concatenated_string = concatenate_strings(input_list)
print(concatenated_string)
