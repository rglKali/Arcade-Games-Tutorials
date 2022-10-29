import random

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SCREEN_TITLE = "2048"


class Cell(arcade.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.center_x = (x + 0.5) * 10
        self.center_y = (y + 0.5) * 10
        self.texture = arcade.load_texture(f'resources/{number}.png')


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.cells = None
        self.grid = None

    def create_new_cell(self, number=None, position=None):
        if not number:
            number = random.choices([2, 4], [9, 1])[0]
        if not position:
            possible_positions = list()
            for y in range(4):
                for x in range(4):
                    if self.grid[x][y] == 0:
                        possible_positions.append((x, y))
            position = random.choice(possible_positions)

        x, y = position
        cell = Cell(x, y, number)
        self.cells.append(cell)
        self.grid[x][y] = number

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.cells = arcade.SpriteList()
        self.grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def on_draw(self, pixelated=True):
        arcade.start_render()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


def main():
    """ Main function """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
