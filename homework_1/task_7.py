inputA = int(input("Введите сколько киллометров спортсмен пробежал в первый день "))
inputB = int(input("Сколько киллометров нужно пробежать "))
day = 1
today = inputA

while True:
    if int(today) == inputB:
        break
    today *= 1.1
    day += 1

print(day)
