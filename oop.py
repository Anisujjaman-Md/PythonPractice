class Person:
    def __init__(self, name: str, date_of_birth: int, height: int = None):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__height = height

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry, Name Can't have number")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        pass
        # return f"Name: {self.__name} , Date of birth: {self.__date_of_birth}, " \
        #        f"height:{self.__height if self.__height is not None else 'Invalid'}"


person_list = [Person("Anis", 1990, 63),
               Person("Shamim", 1490),
               Person("Sumaiya", 1090, 63),
               Person("Rezaul", 1998),
               Person("Asma", 2020, 63)]

# for person in person_list:
#     if person.get_date_of_birth() >= 1980:
#         print(person.get_summary())

class Student(Person):
    def __init__(self, name: str, date_of_birth: int, email: str, student_id: str):
        super().__init__(name, date_of_birth)
        self.email = email
        self.student_id = student_id

    def get_summary(self):
        return f"Name: {self.get_name()} Email: {self.email} Birth date: {self.get_date_of_birth()}"

    def __str__(self):
        return self.get_summary()
    def __repr__(self):
        return self.get_summary()

student1 = Student("Anis", 1992, "Contact.anisujjaman", "172-35-2203")

# print(student1)
#
# student1.set_name("Md Anisujjaman")
#
# print(student1)

class Teacher(Person):
    def __init__(self, name: str, date_of_birth: int, department: str):
        super().__init__(name, date_of_birth)
        self.department = department

    def get_summary(self):
        return f"{self.get_name()} is a teacher"

new_person_list = [Person("Anis", 1997),
                   Student("Sumaiya", 2002 , "Gmail.com", "Id"),
                   Teacher("Shamim", 1992, "Physics")]

for person in new_person_list:
    print(person.get_summary())