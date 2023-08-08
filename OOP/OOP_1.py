class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f"- {department.get_department_name()}")

class Department(University):
    def __init__(self, name, location, department_name, head_of_department):
        super().__init__(name, location)
        self.__department_name = department_name
        self.__head_of_department = head_of_department
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def get_department_name(self):
        return self.__department_name

    def display_details(self):
        print(f"Department Name: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses:
            print(f"- {course}")


if __name__ == "__main__":
    # Create a University
    university = University("Jain University", "Bangalore")

    # Create Departments and Courses
    department1 = Department("Jain University", "Bangalore", "Computer Science", "Dr. Mahesh")
    department1.add_course("Introduction to Programming")
    department1.add_course("Database Management")
    
    department2 = Department("Jain University", "Bangalore", "Physics", "Dr. Naveen")
    department2.add_course("Classical Mechanics")
    department2.add_course("Quantum Physics")

    # Add Departments to the University
    university.add_department(department1)
    university.add_department(department2)

    # Display University and Department Details
    university.display_details()
    print("\nDepartment Details:")
    for department in university._University__departments:
        department.display_details()
        print()
