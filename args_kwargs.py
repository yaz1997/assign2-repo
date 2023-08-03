# *args 1

def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4, 5))   
print(sum_numbers(-1, -2, -3))                    
print(sum_numbers(3.14, 2.71))    


# *args 2
def concat_strings(*args):
    return "".join(args)


print(concat_strings("Assignment", " ", "2"))  
print(concat_strings("This", " ", "is", " ", "for", " ", "*args")) 



#  *kwargs 1

def calculate_total_cost(**kwargs):
    total_cost = sum(kwargs.values())
    return total_cost

print(calculate_total_cost(item1=10, item2=20, item3=5)) 
print(calculate_total_cost(apple=2, banana=3, orange=4, mango=5))  
print(calculate_total_cost(laptop=800, phone=600, headphones=100))  


#  *kwargs 2

def create_student_report(name, age, **subjects_scores):
    report = {
        "name": name,
        "age": age,
        "subjects": subjects_scores
    }
    return report

report = create_student_report("Riyaz", 18, math=95, science=85, history=75)
report2 = create_student_report("Ashray", 15, math=75, science=80, history=90)
print(report, report2)


# def create_student_report(name, age, **subjects_scores):
#     report = {
#         "name": name,
#         "age": age,
#         "subjects": []
#     }

#     For subject, score in kwargs.items():
#     student_info["subjects"].append


