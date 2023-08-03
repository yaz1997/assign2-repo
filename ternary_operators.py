#  TO 1

def check_odd_even(number):
    result = "Even" if number % 2 == 0 else "Odd"
    return result
print(check_odd_even(67))  
print(check_odd_even(100))   
print(check_odd_even(0))   
print(check_odd_even(-79))  


# TO 2

def check_leap_year(year):
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return "Leap Year" if is_leap_year else "Not a Leap Year"

print(check_leap_year(2023))
print(check_leap_year(2024))
print(check_leap_year(2025))
print(check_leap_year(2026))
print(check_leap_year(2027))


# TO 3

def find_bigger_number(num1, num2, num3):
    result = "Equal" if num1 == num2 == num3 else max(num1, num2, num3)
    return result

print(find_bigger_number(15, 65, 5))
print(find_bigger_number(100, 200, 300))


