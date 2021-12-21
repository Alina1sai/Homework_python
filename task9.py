def sort_v(list_a):
        for i in range(1, len(list_a)):
            element = list_a[i]
            index_a = i - 1
            while index_a >= 0 and list_a[index_a] > element:
                list_a[index_a + 1] = list_a[index_a]
                index_a -= 1
            list_a[index_a + 1] = element


if __name__ == '__main__':
    list_a = ([int(numbers) for numbers in input("Введите строку для сортировки вставками: ").split()])
    sort_v(list_a)
    print(list_a)