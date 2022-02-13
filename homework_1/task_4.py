inputInt = int(input("Введите число "))
divider = 1
maxValue = 0
iterator = 0

while True:
    x = int(inputInt / divider % 10)
    inputInt -= x
    divider *= 10
    iterator += 1
    if maxValue < x:
        maxValue = x
    if len(str(inputInt)) == iterator:
        break

print(maxValue)
