from library import Circle, Triangle

circle = Circle(5)     #Радиус
print(f"Площадь круга = {circle.square()}")

triangle = Triangle(2, 2, 3)
print(f"Площадь Треугольника = {triangle.square()}")
print(f"Прямоугольный ли это треугольник ? {triangle.is_right()}")