class Student:

  university = 'New York Academy'

  def __init__(self, name, last, age):
    self.name = name
    self.last = last
    self.age = age
    self.email = name + '.' + last + 'university.com'

obj_anna = Student('anna', 'kowalska', 23)

print(obj_anna.university)

print(Student.university)

print(obj_anna.__dict__) # nie zawiera university
print(Student.__dict__)  # klasa zawiera wartość university
