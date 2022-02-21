my_list = []
input_int = int(input("Введите число элементов "))
i = 0

while len(my_list) < input_int:
    my_list.append(int(input("Введите число")))

print(my_list)

for i in range(0, len(my_list) - 1, 2):
    my_list.insert(i, my_list[i + 1])
    my_list.pop(i + 2)

print(my_list)
