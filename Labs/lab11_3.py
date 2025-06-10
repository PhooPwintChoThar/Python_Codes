class Name(object):
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return self.title + ". " + self.firstName + " " + self.lastName


class Date(object):
    def __init__(self, day, month, year):
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)

    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return self.day + "/" + self.month + "/" + self.year

    def getDateBC(self):
        return self.day + "/" + self.month + "/" + str(int(self.year) + 543)


class Address(object):
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = str(postcode)

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return (
            self.houseNo
            + ", "
            + self.street
            + ", "
            + self.district
            + ", "
            + self.city
            + ", "
            + self.country
            + ", "
            + self.postcode
        )


class Department(object):
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList

    def addEmployee(self, e):
        e.department = self
        self.employeeList.append(e)

    def deleteEmployee(self, e):
        e.department = None
        if e in self.employeeList:
            self.employeeList.remove(e)

    def setManager(self, e):
        if isinstance(e, PermEmployee) and e in self.employeeList:
            self.manager = e
        else:
            print("Manager must be a permanent employee and part of the employee list.")


class Person(object):
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def printinfo(self):
        print(f"Name: {self.name}\nBirthdate: {self.birthdate}\nAddress: {self.address}")


class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department=None):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = department

    def printinfo(self):
        super().printinfo()
        print(f"StartDate: {self.startDate}\nDepartment: {self.department.description if self.department else 'None'}")


class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, wage):
        super().__init__(name, birthdate, address, startDate)
        self.wage = int(wage)

    def printinfo(self):
        super().printinfo()
        print(f"Wage: {self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, salary):
        super().__init__(name, birthdate, address, startDate)
        self.salary = int(salary)

    def printinfo(self):
        super().printinfo()
        print(f"Salary: {self.salary}")


name = Name("Mr", "John", "Doe")
birthdate = Date(15, 6, 1990)
print(birthdate.getDateBC
address = Address("123", "Main St", "Downtown", "Metropolis", "USA", "12345")

person = Person(name.getFullName(), birthdate.getDate(), address.getAddress())
person.printinfo()

department = Department("Software ", None, [])

employee1 = Employee(name.getFullName(), birthdate.getDate(), address.getAddress(), "2020-01-01")
temp_employee = TempEmployee(name.getFullName(), birthdate.getDate(), address.getAddress(), "2022-01-01", 20)
perm_employee = PermEmployee(name.getFullName(), birthdate.getDate(), address.getAddress(), "2019-01-01", 50000)

department.addEmployee(employee1)
department.addEmployee(temp_employee)
department.addEmployee(perm_employee)

employee1.printinfo()
temp_employee.printinfo()
perm_employee.printinfo()

department.setManager(perm_employee)
department.setManager(temp_employee)

department.deleteEmployee(employee1)
department.deleteEmployee(temp_employee)

print("Manager:", department.manager.name if department.manager else "None")
print("Employees in department:")
for emp in department.employeeList:
    print(emp.name)
