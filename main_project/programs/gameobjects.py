#определение високосного года
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#нахождение факториала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)