tems = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    # Проходимо по відсортованому списку і вибираємо страви, поки не перевищимо бюджет
    for item, info in items_sorted:
        if total_cost + info['cost'] <= budget:
            total_cost += info['cost']
            total_calories += info['calories']
            chosen_items.append(item)

    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Створюємо таблицю для зберігання максимальних калорій для кожного бюджету
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    item_list = list(items.items())

    # Заповнюємо таблицю динамічного програмування
    for i in range(1, n + 1):
        item_name, info = item_list[i - 1]
        item_cost = info['cost']
        item_calories = info['calories']

        for b in range(budget + 1):
            if item_cost > b:
                dp[i][b] = dp[i - 1][b]  # Якщо не можемо взяти цей продукт
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - item_cost] + item_calories)

    # Тепер відтворимо вибір продуктів
    total_calories = dp[n][budget]
    total_cost = 0
    chosen_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:  # Якщо продукт був вибраний
            item_name, info = item_list[i - 1]
            chosen_items.append(item_name)
            total_cost += info['cost']
            b -= info['cost']

    return chosen_items, total_calories, total_cost

if __name__ == "__main__":
    budget = 100
    # Приклад використання
    chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
    print(f"Динамічне програмування: {chosen_items}, калорії: {total_calories}, вартість: {total_cost}")

    # Приклад використання

    chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
    print(f"Жадібний алгоритм: {chosen_items}, калорії: {total_calories}, вартість: {total_cost}")