import functions
from functions import greet_user

functions.greet_user("peter", "chen")
greet_user("peter", "chen")


# define classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

point = Point(10, 20)
point.x = 11
print(point.x)
