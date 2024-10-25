import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    # Створюємо словник для підрахунку частот появи кожної суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Імітуємо кидки двох кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Кидок першого кубика
        die2 = random.randint(1, 6)  # Кидок другого кубика
        total = die1 + die2  # Сума чисел на обох кубиках
        sums_count[total] += 1

    return sums_count

# Функція для обчислення ймовірностей на основі частот
def calculate_probabilities(sums_count, num_rolls):
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    return probabilities

# Функція для відображення результатів у вигляді графіка
def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створюємо стовпчиковий графік
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума на двох кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум чисел на двох кубиках (Монте-Карло)')
    plt.xticks(sums)
    plt.show()

# Головна функція для запуску симуляції
def main():
    num_rolls = 100000  # Кількість кидків

    # Імітуємо кидки кубиків
    sums_count = simulate_dice_rolls(num_rolls)

    # Обчислюємо ймовірності для кожної суми
    probabilities = calculate_probabilities(sums_count, num_rolls)

    # Виводимо ймовірності для кожної суми
    print("Ймовірності для кожної суми:")
    for sum_val, prob in probabilities.items():
        print(f"Сума {sum_val}: ймовірність {prob:.4%}")

    # Відображаємо графік ймовірностей
    plot_probabilities(probabilities)

# Запуск програми
if __name__ == "__main__":
    main()