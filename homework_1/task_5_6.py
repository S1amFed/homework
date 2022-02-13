revenue = int(input('Введите выручку '))
costs = int(input('Введите издержку '))

if revenue > costs:
    print('Прибыль — выручка больше издержек')
    print(f'Рентабильность: {revenue / costs}')
    employees = int(input("Введите число сотрудников "))
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {revenue / employees}')
else:
    print('Убыток — издержки больше выручки')
# Третьего не дано по условию задачи
