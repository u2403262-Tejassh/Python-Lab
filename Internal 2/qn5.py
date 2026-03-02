'''
5. Develop a program to model an Employee management system.
i. Create a base class Person with suitable attributes and a method display_details().
ii. Create a derived class Employee with attributes: employee_id, department,
designation, experience, and salary.

Implement the following in Employee class:

 promote () – Promote Assistant Manager to Manager only if experience ≥ 10 years;
otherwise raise a user-defined exception.
 increment() – Increase salary by 10% for Sales, 7% for Marketing, and 5% for others.
 display_details() to show complete details.
Accept details of 5 employees, store them in a list, apply promotion and increment, and
display the updated details sorted by salary (highest first).
'''
class PromoteException(Exception):
    """Exception raised when an employee does not meet promotion criteria."""
    def __init__(self, message="Employee does not meet the requirements for promotion"):
        self.message = message
        super().__init__(self.message)

class Person:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex
    def display_details(self):
        print(f"\nPersonal Details:\nName: {self.name}, Age: {self.age}, Sex: {self.sex}\n")
        
class Employee(Person):
    def __init__(self, name: str, age: int, sex: str, emp_id: int, dept: str, desig: str, exp: int, sal: int):
        super().__init__(name, age, sex)
        self.emp_id = emp_id
        self.dept = dept
        self.desig = desig
        self.exp = exp
        self.sal = sal
    def promote(self):
        if self.exp >= 10*12 and self.desig == "Assistant Manager":
            self.desig = "Manager"
        else:
            raise PromoteException(f"Cannot Promote {self.name}: Requirements not met.")
    def increment(self):
        if self.dept == "Sales":
            self.sal += self.sal*0.1
        elif self.dept == "Marketing":
            self.sal += self.sal*0.07
        else:
            self.sal += self.sal*0.03
    def display_details(self):
        super().display_details()
        print(f"Employee Details:\nEmployee ID: {self.emp_id}, Department: {self.dept}, Designation: {self.desig}, Experience: {self.exp} Months, Salary: {self.sal} Rupees\n")
        print("---------------------------------------------------------------")
E1 = Employee("Alice",32,"F",123,"Marketing","Assistant Manager",11*12, 100000)
E2 = Employee("John",36,"M",105,"Sales","Manager",12*12, 200000)
E3 = Employee("Chris",29,"M",123,"Accounting","Senior Accountant",9*12, 180000)
E4 = Employee("Bibi",37,"M",67,"Human Resources","Assistant Manager",9*12, 250000)
E5 = Employee("Emma",26,"F",123,"Research & Development","Junior Developer",4*12, 80000)
emp_list = [E1, E2, E3, E4, E5]

for i in emp_list:
    try:
        i.promote()
    except PromoteException as e:
        print(f"Alert: {e}")
    i.increment()
sorted_sal_dsc = sorted(emp_list, key=lambda emp: emp.sal, reverse=True)
for i in sorted_sal_dsc:
    i.display_details()
