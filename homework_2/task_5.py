rating = [7, 5, 3, 3, 2]
input_int = int(input("Введите число"))

print(rating)
rating.append(input_int)
rating.sort()
rating.reverse()
print(rating)
