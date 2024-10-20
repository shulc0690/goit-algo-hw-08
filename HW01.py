import heapq


def min_cost_to_connect_cables(cables):
    # Ініціалізація мін-купи
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Беремо два найменших елементи з купи
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)

        # З'єднуємо
        cost = first_min + second_min

        # Додаємо отриманий новий кабель назад у купу
        heapq.heappush(cables, cost)

        # Додаємо витрати з'єднання до загальних витрат
        total_cost += cost

    return total_cost


# Набір кабелів
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
