import math
def square(side):
    area = side * side
    return math.ceil(area)

print(square(4))
print(square(4.2))
print(square(3.1))
print(square(5))