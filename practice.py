# This is a file where I will mess with stuff I learned

# Classes
class Employee:

    # class variables are instantiated here
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # for this class variable, we should use the class instead of an instance because there is no real reason why the number of employees should be
        # different on an instance-to-instance basis
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # class variables can either be implemented using an instance of the class (self)
        # note: when using this method, if the class variable is changed for a specific instance, that change will be taken into account here
        self.pay = int(self.pay * self.raise_amount)
        # or they can be implemented using the class itself (the name of the class)
        # self.pay = int(self.pay * Employee.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Quinn', 'Fredrick', 76500)
emp_2 = Employee('Bart', 'Samuels', 43000)

#class variable changes before and after instantiation
print(Employee.num_of_emps)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
# the line above can also be ran using the class
# if doing this, the instance must be passed as a parameter for the method
print(Employee.fullname(emp_1))

# can change a class variable for a certain instance by just setting it to a new value
# after this is done, the class variable for this specific instance can be seen in the instance's dict as an instance variable of sorts
emp_1.raise_amount = 1.05

# can check the instance variables of a class using __dict__
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)