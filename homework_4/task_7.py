def count(figure):
    current = 1
    factorial = 1
    while current != figure + 1:
        factorial = factorial * current
        yield factorial
        current += 1


for el in count(int(input("Введите число: "))):
    print(el)
