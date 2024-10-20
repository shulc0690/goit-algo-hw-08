import heapq


def merge_k_lists(lists):
    # Використовуємо heapq.merge для об'єднання списків
    merged = heapq.merge(*lists)
    return list(merged)


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6], [1, 2, 6]]

print("Об'єднаний відсортований список:", merge_k_lists(lists))
