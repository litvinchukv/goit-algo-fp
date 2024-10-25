import matplotlib.pyplot as plt
import numpy as np

# Функція для малювання дерева
def draw_pythagoras_tree(x, y, angle, length, level):
    if level == 0:
        return

    # Обчислюємо нові координати для гілки
    new_x = x + length * np.cos(np.radians(angle))
    new_y = y + length * np.sin(np.radians(angle))

    # Малюємо лінію
    plt.plot([x, new_x], [y, new_y], color="green")

    # Рекурсивно малюємо гілки
    draw_pythagoras_tree(new_x, new_y, angle - 30, length * 0.7, level - 1)
    draw_pythagoras_tree(new_x, new_y, angle + 30, length * 0.7, level - 1)

# Основна функція
def main():
    level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 8): "))
    plt.figure(figsize=(8, 6))

    # Початкові координати та кут
    draw_pythagoras_tree(0, 0, 90, 100, level)

    # Налаштування осей
    plt.xlim(-200, 200)
    plt.ylim(0, 300)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()