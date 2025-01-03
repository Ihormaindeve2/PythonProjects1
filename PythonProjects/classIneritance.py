class SchoolMember:
    '''Represents any school memeber'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: ', self.name)
    def tell(self):
        '''Tell any details'''
        print('Name: ', self.name, 'Age:', self.age)

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: ', self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: ', self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student: ', self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: ', self.marks)

t = Teacher('Mrs. Swaroop', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]

for member in members:
    member.tell() #Works for all classes