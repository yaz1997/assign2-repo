# comprehension 1

def filter_long_strings(strings_list):
    return [s for s in strings_list if len(s) > 5]

input_list = ["Riyaz", "Gunjan", "Bipin", "Rojesh", "Ujjwal", "Prateek"]
filtered_list = filter_long_strings(input_list)
print(filtered_list)


#  comprehension 2

def multiply_lists(list1, list2):
    return [x * y for x, y in zip(list1, list2)]

list1 = [42, 27, 63, 84]
list2 = [10, 23, 93, 34]
result_list = multiply_lists(list1, list2)
print(result_list)


# dict_comprehension 1

def create_dictionary(keys, values):
    return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

keys_list = ["name", "age", "city"]
values_list = ["Riyaz", 26, "KTM"]
result_dict = create_dictionary(keys_list, values_list)
print(result_dict)


# dict comprehension 2

def filter_students_above_80(scores_dict):
    return {name: score for name, score in scores_dict.items() if score > 80}

students_scores = {
    "John": 75,
    "Alice": 95,
    "Bob": 85,
    "Emily": 78,
    "Mark": 92
}

filtered_students = filter_students_above_80(students_scores)
print(filtered_students)


# List_comprehension 1

def unique_even_numbers(numbers_list):
    return {num for num in numbers_list if num % 2 == 0}


numbers_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 10]
unique_even_set = unique_even_numbers(numbers_list)
print(unique_even_set)


# list_comprehension 2

def unique_characters(words_list):
    return {char for word in words_list for char in word}


words_list = ["hello", "world", "python", "programming"]
unique_chars_set = unique_characters(words_list)
print(unique_chars_set)
