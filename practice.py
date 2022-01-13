# This is a file where I will mess with stuff I learned

# Classes
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Quinn', 'Fredrick', 76500)
emp_2 = Employee('Bart', 'Samuels', 43000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
# the line above can also be ran using the class
# if doing this, the instance must be passed as a parameter for the method
print(Employee.fullname(emp_1))