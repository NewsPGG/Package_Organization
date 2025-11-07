def bubble_sort(list_numbers):
    # Создаём флаг для проверки окончания алгоритма
    flag = 1
    while flag:
        flag = 0
        # Проходимся по всем элементам данного списка чисел
        for i in range(len(list_numbers) - 1):
            # Если элемент больше следующего, меняем их
            if list_numbers[i] > list_numbers[i + 1]:
                list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
                flag = 1
    return list_numbers