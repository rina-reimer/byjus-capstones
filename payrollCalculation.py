## Payroll Calculation
# ABC Finance company hired you as a software developer. 
# Your first assignment is to create a simple Payroll System for the company to perform payroll calculations based on an employee inheritance hierarchy that meets the following requirements:
    # The company has Salaried employees and they are paid a fixed salary regardless of the number of hours they work. 
    # Their salary is calculated by adding the basic salary, TA (Travelling allowance), DA (Dearness allowance) and HRA (House rent allowance).
    # To make the system reusable and extensible, the system must be constructed using object-oriented methodology.
#  Create class 'Employee'. Add constructor to initialise variables. Add getter and setter functions.

# class 'Employee'
class Employee:
    def __init__(self, empid, empname, ssn):
        self.__empid = empid
        self.__empname = empname
        self.__ssn = ssn
        self.__income = 0
    def get_empid(self):
        return self.__empid
    def get_empname(self):
        return self.__empname
    def get_ssn(self):
        return self.__ssn
    def get_income(self):
        return self.__income
    def set_empname(self, newname):
        self.__empname = newname
    def set_income(self, new_income):
        self.__income = new_income
    def __repr__(self):
        return "Name: "+str(self.__empname)+", ID: "+str(self.__empid)+", SSN: "+str(self.__ssn)+", Income: "+str(self.__income)

class SalariedEmployee(Employee):
    def __init__(self, empid, empname, ssn):
        super().__init__(empid, empname, ssn)    
        self.__ta = 500
        # Initialise the instance variable for dearness allowance with any value
        self.__da = 500
        # Initialise the instance variable for house rent allowance with any value
        self.__hra = 500
        self.__income = 0
    def get_ta(self):
        return self.__ta
    def get_hra(self):
        return self.__hra
    def get_da(self):
        return self.__da
    def set_ta(self,new_ta):
        self.__ta = new_ta
    def set_da(self,new_da):
        self.__da = new_da
    def set_hra(self,new_hra):
        self.__hra = new_hra
    # Override
    def calculate_income(self):
        basic = int(input("What's the basic salary? "))
        self.set_income(basic + self.__ta + self.__da + self.__hra)
        print(self.__income)

class Management:
  emp_id_list = []
  emp_records = []
 
  @classmethod
  def existing_employee(cls, emp_id):
    for i in Management.emp_id_list:
      while i == emp_id:
        print("This employee ID already exists")
        return 0
    Management.emp_id_list.append(emp_id)
    return 1
  @classmethod
  def add_records(cls, employee):
    employ = {}
    employ["Employee ID"]=employee.get_empid()
    employ["Employee Name"]=employee.get_empname()
    employ["SSN"]=employee.get_ssn()
    employ["Salary"]=employee.get_income()
    Management.emp_records.append(employ)
  @classmethod
  def display_records(cls):
    for i in Management.emp_records:
      for j in i:
        print(f"{j} : {i[j]}")
      print("------------------------------------")
    print("***************************************")

## Functionality
while True:
  id = input("Enter employee ID: ")
  manage = Management()

  while manage.existing_employee(id) == 0:
    print("Please enter a new employee id ")
    id = input("Enter employee ID: ")
  name = input("Enter employee name: ")
  ssn = input("Enter social security number: ")
    
  emp1 = SalariedEmployee(id, name, ssn)
    
  while True:
    print(f"\nTravelling allowance is {emp1.get_ta()}\nDearness allowance is {emp1.get_da()}\nHouse Rent allowance is {emp1.get_hra()}\n")
    print("-----Enter your choice------")
    user_choice = input("Enter 1 for updating Travelling allowance(TA)\nEnter 2 for updating Dearness allowance(DA)\nEnter 3 for updating House Rent allowance(HRA)\nEnter 4 to skip updating: ")
    while user_choice not in ['1','2','3','4']:
      print("-----Please enter a valid option------")
      user_choice = input("Enter 1 for updating Travelling allowance(TA)\nEnter 2 for updating Dearness allowance(DA)\nEnter 3 for updating House Rent allowance(HRA)\nEnter 4 to skip updating: ")
     
    if user_choice == '1':
      new_ta = int(input("\nEnter the new Travelling Allowance: "))
      emp1.set_ta(new_ta)
      print(f"Travelling allowance is {emp1.get_ta()}\n")
    elif user_choice == '2':
      new_da = int(input("Enter the new Dearness Allowance: "))
      emp1.set_da(new_da)
      print(f"Dearness allowance is {emp1.get_da()}\n")
    elif user_choice == '3':
      new_hra = int(input("Enter the new House Rent Allowance: "))
      emp1.set_hra(new_hra)
      print(f"House Rent allowance is {emp1.get_hra()}\n")
    else:
      break      
    print("----------------------------------------")
      
    choice = int(input("Do you wish to continue updating TA, DA or HRA?\nEnter 1 for YES\nEnter 2 for NO\n"))
 
    if choice == 2:
      break

   
  print(f"\n--------Calculating Income----------------")  
  emp1.calculate_income()
  print("\n--------Employee Details----------------")
  print(emp1)
  print("\n----------------------------------------")
  Management.add_records(emp1)
  choice_display=int(input("\nView All Records?\nEnter 1 for YES\nEnter 2 for NO\n"))
  if choice_display == 1:
    print("Employee Records")
    print("\n----------------------------------------")
    Management.display_records()

  choice=int(input("\nDo you wish to continue?\nEnter 1 for YES\nEnter 2 for NO\n"))
 
  if choice == 2:
    print("Thank you")
    
    break