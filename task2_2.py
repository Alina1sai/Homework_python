import math

def circle(r): #площадь круга через радиус круга
    result = math.pi * r ** 2
    return result

def polygon(a, n):  # площадь правильного многоугольника через сторону
    result = (a ** 2 * n) / (4 * math.tan(math.pi / n))
    return result

def triangle (a, h):  # площадь треугольника по стороне и высоте
    result = 1/2 * a * h
    return result

def  rectangle (a, b):  # площадь прямоугольника
    result = a * b
    return result

def trapeze(a, b, h):  # площадь трапеции через основания и высоту
    result = (a + b) * h / 2
    return result


f = int(float(input("Введите номер необходимой команды: \n"
                    "1 - площадь круга через радиус круга \n"
                    "2 - площадь правильного многоугольника через сторону \n"
                    "3 - площадь треугольника по стороне и высоте \n"
                    "4 - площадь прямоугольника \n"
                    "5 - площадь трапеции через основания и высоту \n")))

if f == 1:
    r = float(input("Введите радиус круга: "))
    print("Площадь круга: ", round(circle(r), 3))

elif f == 2:
    a = float(input("Введите длину стороны: "))
    n = int(input("Введите количество сторон: "))
    print("Площадь правильного многоугольника: ", round(polygon(a, n), 3))

elif f == 3:
    a = float(input("Введите длину стороны: "))
    h = float(input("Введите длину высоты, проведенную к этой стороне: "))
    print("Площадь треугольника: ", round(triangle (a, h), 3))

elif f == 4:
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    print("Площадь прямоугольника: ", round(rectangle (a, b), 3))

else:
    a = float(input("Введите первое основание: "))
    b = float(input("Введите второе основание: "))
    h = float(input("Введите высоту: "))
    print("Площадь трапеции: ", round(trapeze(a, b, h), 3))