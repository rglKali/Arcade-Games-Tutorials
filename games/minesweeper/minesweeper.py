import arcade
import random


# Создаём класс Cell с наследованием класса Sprite
class Cell(arcade.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        # Флаг bomb означает, есть ли в клетке бомба
        self.is_bomb = False

        # Флаг open означает, клетка ли уже открыта, или ещё нет
        self.is_open = False

        # Флаг flag означает, отмечена ли данная клетка флажком
        self.is_flag = False

        # Присваиваем клетке её координаты
        self.center_x = (x + 0.5) * 32
        self.center_y = (y + 0.5) * 32

        # Загружаем текстуру с помощью метода load_texture
        self.texture = arcade.load_texture('resources/cell.png')


# Создаём основной класс Game класс с наследованием класса Window
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=640, height=640, title='Minesweeper')

        # Создаём список, который потом заполним клетками
        self.cells = arcade.SpriteList()

    def setup(self):

        # Создаём поле 20х20
        for x in range(20):
            for y in range(20):

                # Вызываем объект клетки, передавая в неё координаты х и у
                cell = Cell(x, y)

                # С шансом в 10% кладём в эту клетку бомбу
                cell.is_bomb = random.choices([False, True], [9, 1])[0]

                # Добавляем созданную клетку в наш список
                self.cells.append(cell)

    def reveal(self, cell: Cell):
        # Проверим, является ли клетка уже открытой с флажком
        # В этих случаях мы не можем с ней взаимодействовать
        if cell.is_open or cell.is_flag:

            # Если так, то пропускаем
            pass
        else:
            # Если нет, открываем нашу клетку

            cell.is_open = True

            # Проверяем, есть ли в этой клетке бомба
            if cell.is_bomb:

                # Если в клетке есть бомба, обновляем текстуру
                cell.texture = arcade.load_texture('resources/bomb_active.png')
                pass
            else:

                # Если в клетке нет бомбы, то нам нужно узнать, сколько бомб находятся в соседних клетках
                # Для этого создадим список, куда будем помещать все клетки, которые находятся рядом
                neighbors = list()

                # И запустим цикл через все клетки на поле, чтобы выявить соседние
                for neighbor in self.cells:

                    # Соседние клетки можно вычислить, измерив расстояние между клетками
                    # Если расстояние по Х и расстояние по У меньше размера самой клетки,
                    # Значит эти две клетки находятся рядом друг с другом
                    # Расстояние можно найти, взяв модуль от разницы координат наших объектов
                    if abs(cell.center_x - neighbor.center_x) <= 32 and abs(cell.center_y - neighbor.center_y) <= 32:

                        # Если клетки являются соседними, заносим эту клетку в список соседей
                        neighbors.append(neighbor)

                # Объявлю переменную, которая будет хранить в себе количество бомб в соседях
                bombs = 0

                # Теперь запустим цикл по соседям, чтобы выяснить, во скольких из них есть бомбы
                for neighbor in neighbors:

                    # Проверяем соседа на наличие бомбы
                    if neighbor.is_bomb:

                        # Если есть бомба, увеличиваем количество бомб на 1
                        bombs += 1

                # Теперь нам нужно обновить текстуру нашей клетки
                # Для этого открываем текстуру под нужным номером - количеством бомб в округе
                cell.texture = arcade.load_texture(f'resources/{bombs}.png')

                # Так же, если вокруг нашей клетки нет ни одной бомбы, нам нужно автоматически открыть все соседние клетки
                if bombs == 0:
                    for neighbor in neighbors:
                        self.reveal(neighbor)

    def game_over(self):
        pass

    def on_draw(self):
        # Необходимая команда, чтобы запустить движок
        arcade.start_render()

        # Команда для отрисовки всех клеток нашего списка
        self.cells.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # Получим объект, на который тыкнул игрок
        cell = arcade.get_sprites_at_point((x, y,), self.cells)[0]

        # Проверим, какой кнопкой мыши игрок нажал на клетку
        if button == arcade.MOUSE_BUTTON_RIGHT:

            # Проверим, является ли эта клетка уже открытой
            if cell.is_open:

                # Если клетка уже открыта, пропускаем
                pass

            else:

                # Если клетка ещё не открыта, нам нужно убрать / поставить флажок
                if cell.is_flag:

                    # На клетке уже висит флажок, так что мы должны его снять
                    cell.is_flag = False

                    # Так же не забываем обновить текстуру
                    cell.texture = arcade.load_texture('resources/cell.png')
                else:

                    # На клетке нет флажка, значит мы должны его поставить
                    cell.is_flag = True

                    # И обновить текстуру
                    cell.texture = arcade.load_texture('resources/flag.png')
        else:

            # Если это левая кнопка, то вызываем функцию открытия клетки
            self.reveal(cell)


# Основная функция для запуска программы
def main():
    # Создаём наше окно
    game = Game()
    # Запускаем программу
    game.setup()
    # Запускаем движок
    arcade.run()


if __name__ == '__main__':
    # Вызываем основную функцию и запускаем программу
    main()
