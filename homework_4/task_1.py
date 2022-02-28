from sys import argv


def count():
    name, work_hours, money, premium = argv
    return int(work_hours) * int(money) + int(premium)


print(count())
