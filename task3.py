num1 = int(float(input("Введите число: ")))

if num1 <= 2:
    print ("Меньше заданного простого числа не существует")
    exit()
k=0
for i in range (num1-1, 0, -1):
    if k==2 :
        print("Максимальное простое число: ", i+1)
        break
    k=0
    for j in range (1, i+1, 1):
        rest = i % j
        if rest == 0:
            k += 1