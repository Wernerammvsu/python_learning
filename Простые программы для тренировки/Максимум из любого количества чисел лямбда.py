from functools import reduce

n = int(input("Введите количество чисел: "))
arr = [(int(input())) for i in range(n)]
print("Максимумальное число:", reduce(lambda x, y: x if x > y else y, arr))
