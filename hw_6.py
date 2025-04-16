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

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Проверка индекса {mid}, значение {arr[mid]}")

        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target} — ищем справа")
            low = mid + 1
        else:
            print(f"{arr[mid]} > {target} — ищем слева")
            high = mid - 1

    print(f"Элемент {target} не найден.")
    return -1

unsorted_list = [22, 5, 17, 1, 34, 10, 45, 52]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

binary_search(sorted_list, 17)
