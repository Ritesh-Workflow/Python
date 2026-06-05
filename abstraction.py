from abc import ABC , abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculateSalary(self,salary):
        self.salary=salary

class Developer(Employee):
    def calculateSalary(self, salary,bonus):
        self.bonus=bonus
        super().calculateSalary(salary)
        print("Developer Salary :",self.salary+self.bonus)

class Manager(Employee):
    def calculateSalary(self, salary, incentive):
        super().calculateSalary(salary)
        self.incentive=incentive
        print("Manager Salary :",self.salary+self.incentive)

D=Developer()
M=Manager()
D.calculateSalary(50000,10000)
M.calculateSalary(70000,15000)



# class Student(ABC):
#     @abstractmethod
#     def check_result(self,marks,passing_marks):
#         self.marks=marks
#         self.passing_marks=passing_marks

# class Engineering(Student):
#     def check_result(self, marks, passing_marks):
#         super().check_result(marks, passing_marks)
#         print("Engineering Student Pass" if marks>passing_marks else "Engineering Student Fail")

# class Medical(Student):
#     def check_result(self, marks, passing_marks):
#          super().check_result(marks, passing_marks)
#          print("Medical student Pass" if marks>passing_marks else "Medical Student Fail")
        
# engineering=Engineering()
# medical=Medical()
# engineering.check_result(45,40)
# medical.check_result(45,50)
