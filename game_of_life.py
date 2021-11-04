"""game of life game with python and EasyDraw framework
"""

import random
from EasyDraw import EasyDraw

WIDTH = 800
HEIGHT = 800
COUNT = 20
X_DIST = WIDTH // COUNT
Y_DIST = HEIGHT // COUNT

class Population:
    """Population class
    """
    def make_2d_array_random(self) -> list:
        """make 2D array with random value

        Returns:
            list: random 2d array
        """
        arr = [[random.randint(0, 1) for _ in range(COUNT)] for _ in range(COUNT)]
        return arr

    def make_2d_array(self) -> list:
        """make 2D array with const value, will replace with any number

        Returns:
            list: 2d array
        """
        arr = [[1 for _ in range(COUNT)] for _ in range(COUNT)]
        return arr

    def count_live_neighbors(self, x_size: int, y_size: int) -> int:
        """count the live cell in round the cell(x, y)

        Args:
            x (int): x
            y (int): y

        Returns:
            int: count
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                col = (i + x_size + COUNT) % COUNT
                row = (j + y_size + COUNT) % COUNT
                count += self.cells[col][row]
        count -= self.cells[x_size][y_size]
        return count

    def __init__(self):
        self.cells = self.make_2d_array_random()

    def draw(self, canvas):
        """draw the rect in the screen, and make next_gen and do the rules

        Args:
            canvas (application): canvas
        """
        next_gen = self.make_2d_array()
        for i in range(COUNT):
            for j in range(COUNT):
                state = self.cells[i][j]
                canvas.fill('white' if state == 1 else 'black')
                canvas.rect(i * X_DIST, j * Y_DIST,
                            (i+1) * X_DIST, (j+1) * X_DIST)
                count = self.count_live_neighbors(i, j)
                if state == 1 and (not count in (2, 3)):
                    next_gen[i][j] = 0
                elif state == 0 and count == 3:
                    next_gen[i][j] = 1
                else:
                    next_gen[i][j] = state
        self.cells = next_gen
        # time.sleep(20)

def setup(app):
    """setup in EasyDraw

    Args:
        app (app): application
    """
    app.pop = Population()
    app.canvas.stroke('black')

def draw(app):
    """draw app

    Args:
        app (app): application
    """
    app.pop.draw(app.canvas)


EasyDraw(
    width= WIDTH,
    height = HEIGHT,
    fps = 20,
    background = 'black',
    title = 'Game of Life',
    autoClear = True,
    fullscreen = False,
    showStats = False,
    setupFunc = setup,
    drawFunc = draw
)
