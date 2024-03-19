#проверка являетсяли строка палиндромом
def is_palindrome(string):
    return string == string[::-1]

#поиск среднего значения в списке
def find_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    else:
        return total / count