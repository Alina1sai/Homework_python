num = int(float(input("Введите число: ")))

if num < 2:
    print ("Меньше заданного простого числа не существует")
    exit()

k = 0

for i in range (1, num+2, 1):
    if k == 2:
        rest = num % (i-1)
        while rest == 0:
           num = num / (i-1)
           print((i-1))
           rest = num % (i-1)

    k = 0
    for j in range (1, i+1, 1):
        rest = i % j
        if rest == 0:
            k += 1