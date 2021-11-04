"""Game of Life, with python code.
"""
from time import sleep
from random import randint
from EasyDraw import EasyDraw

WIDTH = 800
HEIGHT = 800
COUNT = 20
X_DIST = WIDTH // COUNT
Y_DIST = HEIGHT // COUNT
# Time interval between each generation
INTERVAL_TIME = 0

class Population:
    """Population class
    """

    def __init__(self):
        self.cells = self.make_2d_array_random()
        self.next_cells = self.make_2d_array()

    @staticmethod
    def make_2d_array_random() -> list:
        """make 2D array with random value

        Returns:
            list: random 2d array
        """
        arr = [[randint(0, 1) for _ in range(COUNT)] for _ in range(COUNT)]
        return arr

    @staticmethod
    def make_2d_array() -> list:
        """make 2D array with const value, will replace with any number

        Returns:
            list: 2d array
        """
        arr = [[1 for _ in range(COUNT)] for _ in range(COUNT)]
        return arr

    def count_live_neighbors(self, x_pos: int, y_pos: int) -> int:
        """counting the live cell in round the cell(x, y)

        Args:
            x_pos (int): x
            y_pos (int): y

        Returns:
            int: count
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # `(x + pos + COUNT) % COUNT` means:
                # If the cell leaves the page, count from the other side
                col = (i + x_pos + COUNT) % COUNT
                row = (j + y_pos + COUNT) % COUNT
                # If cell 0 means it is not alive
                # and if cell 1 means it is alive and counted
                count += self.cells[col][row]
        # The current cell is not counted
        count -= self.cells[x_pos][y_pos]
        return count

    def setting_next_generation(self, i, j):
        """Setting the next generation

        Args:
            i (int): i position
            j (int): j position
        """
        count = self.count_live_neighbors(i, j)
        state = self.cells[i][j]
        if state == 1 and (not count in (2, 3)):
            self.next_cells[i][j] = 0
        elif state == 0 and count == 3:
            self.next_cells[i][j] = 1
        else:
            self.next_cells[i][j] = state

    def draw(self, canvas):
        """Drawing the rectangle in the screen,
        creating next generation and doing the rules.

        Args:
            canvas (application.canvas): canvas of screen
        """

        self.next_cells = self.make_2d_array()  # clear next_cells
        for i in range(COUNT):
            for j in range(COUNT):
                state = self.cells[i][j]
                # Adjusting the color of the filler
                canvas.fill('white' if state == 1 else 'black')
                # Drawing the rectangle from i and j to i+1 and j+1
                canvas.rect(i * X_DIST, j * Y_DIST,
                            (i+1) * X_DIST, (j+1) * X_DIST)
                self.setting_next_generation(i, j)

        self.cells = self.next_cells
        sleep(INTERVAL_TIME)


def setup(app):
    """Setting the application

    Args:
        app (EasyDraw.EasyDraw): application variable
    """
    app.population = Population()
    app.canvas.stroke('black')


def draw(app):
    """Drawing the items

    Args:
        app (EasyDraw.EasyDraw): application variable
    """
    app.population.draw(app.canvas)


EasyDraw(
    width=WIDTH,
    height=HEIGHT,
    fps=20,
    background='black',
    title='Game of Life',
    autoClear=True,
    fullscreen=False,
    showStats=False,
    setupFunc=setup,
    drawFunc=draw)
