# exception handling 1

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"The result of {num1} / {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid integers as input.")


# exception handling 2

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    try:
        filename = input("Enter the filename: ")
        display_file_contents(filename)
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# exception handling 3

def convert_to_integer(user_input):
    try:
        num = int(user_input)
        return num
    except ValueError:
        print(f"Error: '{user_input}' cannot be converted to an integer.")
        return None

if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        converted_num = convert_to_integer(user_input)
        if converted_num is not None:
            print(f"The converted integer is: {converted_num}")
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# exception handling 4

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ValueError:
        print("Error: Please enter valid integers as input.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"The result of {num1} / {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid integers as input.")
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
