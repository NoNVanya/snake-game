import os
import random
import time

class SimpleSnake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.width = 20
        self.height = 10
        self.snake = [[5, 5]]
        self.food = self.create_food()
        self.direction = 'd'
        self.score = 0

    def create_food(self):
        while True:
            food = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]
            if food not in self.snake:
                return food

    def draw(self):
        os.system('cls')
        print("=== ЗМЕЙКА ===")
        print("ПРАВИЛА:")
        print("• Управление: W (вверх), A (влево), S (вниз), D (вправо)")
        print("• Q - выход из игры")
        print("• R - перезапуск игры")
        print("• Собирайте * чтобы увеличивать счет")
        print("• Не врезайтесь в стены и в себя")
        print("================")
        print(f"Счет: {self.score}")
        print("+" + "-" * self.width + "+")

        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                if [y, x] in self.snake:
                    line += "O"
                elif [y, x] == self.food:
                    line += "*"
                else:
                    line += " "
            line += "|"
            print(line)

        print("+" + "-" * self.width + "+")

    def move(self):
        head = self.snake[0].copy()

        if self.direction == 'w':
            head[0] -= 1
        elif self.direction == 's':
            head[0] += 1
        elif self.direction == 'a':
            head[1] -= 1
        elif self.direction == 'd':
            head[1] += 1

        # Проверка столкновений
        if (head[0] < 0 or head[0] >= self.height or
                head[1] < 0 or head[1] >= self.width or
                head in self.snake):
            return False

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

        return True

    def play(self):
        while True:
            self.draw()
            move = input("Направление (WASD): ").lower()

            if move == 'q':
                break
            elif move == 'r':
                self.reset()
                continue
            if move in ['w', 'a', 's', 'd']:
                self.direction = move

            if not self.move():
                print("Игра окончена! Нажмите R для рестарта или Q для выхода")
                while True:
                    choice = input().lower()
                    if choice == 'r':
                        self.reset()
                        break
                    elif choice == 'q':
                        return
                    else:
                        print("Неверный ввод. Нажмите R или Q")

if __name__ == "__main__":
    game = SimpleSnake()
    game.play()

if __name__ == "__main__":
    game = SimpleSnake()

    game.play()
