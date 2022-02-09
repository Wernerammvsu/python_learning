n = int(input("Количество чисел: "))
arr = []
for i in range(n):
    arr.append(int(input()))

maximum = arr[0]
for i in range(len(arr)):
    if maximum < arr[i]:
        maximum = arr[i]

print("Максимальное число: ", maximum)
