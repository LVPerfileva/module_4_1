def divide(first, second):
    if second != 0:
        return first / second
    else:
        return "Ошибка"


math_res = divide(15, 4)
print(math_res)
math_res = divide(5, 0)
print(math_res)
