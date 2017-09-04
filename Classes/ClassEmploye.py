class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@email.com"

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # Employee.__init__(self, first, last, pay)


class Manager(Employee):
    def __init__(self, first, last, pay, employess=None):
        super().__init__(first, last, pay)
        if employess is None:
            self.employess = []
        else:
            self.employess = employess

    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employess:
            print('-->', emp.fullname, emp.email, emp.pay)

Employee.set_raise_amt(1.05)

emp_1 = Employee('Alan', 'Wake', 5000)

emp_2 = Employee.from_string('John-Doe-7000')
emp_3 = Employee.from_string('Steve-Wander-8000')
emp_4 = Employee.from_string('Jane-Doe-9000')

dev_2 = Developer('Logan', 'Wolf', 10000, 'Python')
dev_3 = Developer('Tom', 'Tor', 9000, 'Java')
dev_4 = Developer('Alan', 'Lor', 9000, 'Java')
dev_5 = Developer('Greg', 'Kor', 9000, 'Java')
mgr_1 = Manager('Zun', 'Gul', 9000)

# print(issubclass(Manager, Developer))

print(mgr_1.email)
mgr_1.add_emp(emp_1)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(emp_2)
mgr_1.add_emp(emp_3)
mgr_1.add_emp(emp_4)
mgr_1.add_emp(dev_3)
mgr_1.add_emp(dev_4)
mgr_1.add_emp(dev_5)
mgr_1.print_emps()


# dev_2.apply_raise()

# dev_2.fullname = 'Ann Marrie'
#
# print(dev_2.email)
#
# del dev_2.fullname
#
# print(dev_2.email)


# # print(dev_2.pay)
# # print(dev_2.fullname())
# # print(dev_2.prog_lang)

# print(mgr_1)
# print(emp_1.__repr__())
# print(dev_2.__str__())

# print(len(mgr_1))

# print(emp_2)
# emp_2.apply_raise()
# print(emp_2.pay)
# print(emp_3)

# import datetime
# my_date = datetime.date(2016, 7, 11)
#
# print(Employee.is_workday(my_date))
