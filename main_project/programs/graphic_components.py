#перевод градусов Цельсия в градусы Фаренгейта
def celcius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#вычисление площади треугольника (Герон)
def triangle_area(a, b, c):
    s = (a+ b+ c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
