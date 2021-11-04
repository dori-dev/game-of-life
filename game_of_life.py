"""Game of Life, with python code.
"""
from EasyDraw import EasyDraw
from population import Population
from constant import WIDTH, HEIGHT

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
