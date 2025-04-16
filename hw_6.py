# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Обмен элементов
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}")
            return
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print(f"Элемент {target} не найден в списке")

# Несортированный список
unsorted_list = [12, 4, 5, 33, 7, 1, 19, 45]

# Сортируем список
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# Ищем элемент в отсортированном списке
binary_search(7, sorted_list)
