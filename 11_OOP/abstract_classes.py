from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def sides(self): # abstract method
        pass


class Triangle(Shape):

    def sides(self):
        print("I have 3 sides")


class Circle(Shape):

    def sides(self):
        print("I have 0 sides")


class Square(Shape):

    def sides(self):
        print("I have 4 sides")


T = Triangle()
T.sides()

C = Circle()
C.sides()

S = Square()
S.sides()

print('************')

A = Shape()
A.sides()