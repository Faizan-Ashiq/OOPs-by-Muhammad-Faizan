class Employee: 
    company = "Asus" # This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
        self.company = company # this is an instance attribute which overrides the class attribute

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")


a = Employee(3400, "John", 3, "Tesla")
print(a.company) # will always print instance attribute whenever present
# print(Employee.company) # This will always print the class attribute

# # Object introspection 
# print(dir(a))