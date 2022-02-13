inputInt = int(input('Введите количество секунд '))
seconds = inputInt % 60
minute = int(inputInt / 60 % 60)
hours = int(inputInt / 60 / 60 % 60)

print(f'{hours}:{minute}:{seconds}')
