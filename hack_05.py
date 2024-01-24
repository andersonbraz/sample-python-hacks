class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class Employee(Person):
    def __init__(self, name, birth_date, position):
        super().__init__(name, birth_date)
        self.position = position


john = Employee("John Doe", "2001-02-07", "Python Developer")

print("", f"{john.name} - {john.birth_date} - {john.position}")
