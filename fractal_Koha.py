import turtle
import math


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    print()
    print("=== Генератор сніжинки Коха ===")
    print("Задай глибину рекурсії від 1 до 6")
    print("1-2 - Швидко")
    print("3-4 - Помірна складність")
    print("5-6 - Повільно, але красиво")
    print()

    while True:
        try:
            order = int(input("Введіть рівень рекурсії (1-6): "))
            if order < 0:
                print("Рівень не може бути від'ємним!")
                continue
            elif order > 6:
                confirm = input(
                    "Увага! Високі рівні можуть працювати повільно. Продовжити? (y/n): "
                )
                if confirm.lower() != "y":
                    continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    koch_snowflake(order)


if __name__ == "__main__":
    main()
