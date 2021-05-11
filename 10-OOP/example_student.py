class Student:
    pass

obj_anna = Student()
obj_arek = Student()

print(type(obj_anna))
print(type(obj_arek))

obj_anna.email = 'anna.kowalska@com.pl'

print(obj_anna.email)

obj_anna = Student()
obj_anna.name = 'anna'
obj_anna.last = 'kowalska'
obj_anna.age = 23
obj_anna.email = 'anna.kowalska@university.com'

print(obj_anna.name)
print(obj_anna.last)
print(obj_anna.age)
print(obj_anna.email)