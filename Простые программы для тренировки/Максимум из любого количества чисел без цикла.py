n = int(input("Количество чисел: "))
maximum = int(input())
for i in range(n-1):
    curr = int(input())
    if maximum < curr:
        maximum = curr
print("Максимальное число:", maximum)
