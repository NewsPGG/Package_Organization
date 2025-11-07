def quick_sort(array):
    # Если длина массива <= 1, возвращаем его
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2] # Примерно средний элемент данного массива
        # Списки для меньших, больших и равных pivot элементам соответственно
        left, right, equal = [], [], []
        # Проходимся по элементам данного массива и раскидываем их по новым массивам
        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                equal.append(i)
        # Рекурсивно обрабатываем массивы left и right, запоминаем массив equal
        return quick_sort(left) + equal + quick_sort(right)