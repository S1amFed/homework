input_string = input("Введите строку ")
my_list = input_string.split(" ")

for i in range(len(my_list)):
    print(f"{i+1}.{my_list[i][:10]}")
