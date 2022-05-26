def binary_search (list, search_item):
    low = 0
    high = len(list)-1
    search_res = False


    while low<=high and not search_res:
        middle = (low+high)//2
        guess =list[middle]
        if guess == search_item:
            search_res = True
            return search_res
        if guess > search_item:
            high = middle - 1

        else:
            low = middle+1
    return search_res

list = [1, 4, 5, 6, 8, 9, 10, 12]
value = 4
result = binary_search(list, value)
if result:
    print("Элемент найден!")
else:
    print('Элемент не найден')


n = 6
mas = [5, 7, 4, 3, 8, 2]
count = 0
for run in range(n-1):
    for i in range(n-1):
        if mas[i]> mas[i+1]:
            count +=1
            mas[i], mas[i+1] = mas[i+1], mas[i]

    print(mas)
print((count))

