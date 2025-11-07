def merge_sort(array):
    # Если длина массива <= 1, возвращаем его
    if len(array) <= 1:
        return array

    # Находим середину списка и делим его на две половины
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    # Рекурсивно сортируем половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Объединяем отсортированные половины
    return merge(left_sorted, right_sorted)

def merge(left_list, right_list):
    sorted_list = []
    left_index = right_index = 0
    # Сравниваем элементы из списков и добавляем меньший в отсортированный список
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы из левого или правого списка
    sorted_list.extend(left_list[left_index:])
    sorted_list.extend(right_list[right_index:])

    return sorted_list