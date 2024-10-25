import turtle

# Функція для малювання фрактала "дерево Піфагора"
def draw_pythagoras_tree(t, length, level, angle=30):
    # Базовий випадок: якщо рівень рекурсії досяг 0, малюємо лінію
    if level == 0:
        t.forward(length)
        t.backward(length)  # Повертаємося назад до точки початку гілки
        return

    # Малюємо стовбур гілки
    t.forward(length)

    # Зберігаємо поточну позицію та кут черепахи
    pos = t.pos()
    heading = t.heading()

    # Малюємо праву гілку дерева
    t.left(angle)
    draw_pythagoras_tree(t, length * 0.7, level - 1, angle)

    # Повертаємо черепаху до початкової позиції та кута
    t.setpos(pos)
    t.setheading(heading)

    # Малюємо ліву гілку дерева
    t.right(angle)
    draw_pythagoras_tree(t, length * 0.7, level - 1, angle)

    # Повертаємо черепаху до початкової позиції
    t.setpos(pos)
    t.setheading(heading)

# Основна функція для ініціалізації turtle і запуску малювання
def main():
    # Створюємо екран для малювання
    screen = turtle.Screen()
    screen.title("Фрактал: Дерево Піфагора")  # Задаємо заголовок вікна

    # Задаємо розмір вікна (ширина: 800, висота: 600)
    screen.setup(width=800, height=600)

    # Ініціалізація об'єкта Turtle для малювання
    t = turtle.Turtle()
    t.speed(0)  # Встановлюємо максимальну швидкість черепахи
    t.left(90)  # Повертаємо черепаху вгору для початку малювання дерева

    # Запитуємо користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 8): "))

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, 100, level)

    # Команда для коректного завершення малювання та циклу подій
    turtle.done()

# Перевіряємо, чи файл виконується як головна програма
if __name__ == "__main__":
    main()