def binary_search(some_list, target):
    left = 0
    right = len(some_list) -1

    while left <= right:
        mid = left + (right - left) // 2

        if some_list[mid] == target:
            return mid

        elif some_list[mid] < target:
            left = mid + 1

        else:
            left = mid - 1

    return -1


a = [1,2,3,4,5,6,7,8,9,10]
b = 10

result = binary_search(a, b)

if result != -1:
    print(f'Элемент найден на индексе {result}')

else:
    print('Элемент не найден')