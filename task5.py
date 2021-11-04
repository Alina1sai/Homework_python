num = int(float(input("Введите число: ")))

if num < 2:
    print ("Меньше заданного простого числа не существует")
    exit()
k=0
for i in range (num, 0, -1):
    if k==2 :
        print("Максимальное простое число: ", i+1)
        num1, num2 = i+1, i+1
        break
    k=0
    for j in range (1, i+1, 1):
        rest = i % j
        if rest == 0:
            k += 1
k = 0
while k != 15:
    print(num1)
    num1, num2 = num2, num1+num2
    k+=1