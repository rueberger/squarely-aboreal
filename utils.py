""" Utility methods
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches
import seaborn as sns

sns.set_style('white')

def plot_game_state(game_state, fig=None):
    """ Custom plot of the game state
    Each square is represented by two rectangles
    One is always 1 x 1 with color indicating square production
    The other has variable size indicating strength and color indicating ownership

    Args:
      game_state: a game state - GameMap
      fig: optional figure - Figure

    Returns:
      state_plot: visualization of game state - Artist

    """
    fig = fig or plt.figure()
    axis = fig.add_subplot(111)

    prod_z_order = 1
    player_z_order = 2

    production_cmap = sns.color_palette('gray', 256)
    player_cmap = sns.color_palette('husl', game_state.starting_player_count)

    for square in game_state.contents:
        # production square
        production_rect = patches.rectangle((square.x, square.y), 1, 1,
                                            fill=True, color=production_cmap[square.production],
                                            zorder=prod_z_order, visible=True)
        axis.add_patch(production_rect)

        # player square
        rel_size = square.strength /  255
        assert 0 <= rel_size <= 1
        offset = 0.5 - rel_size / 2

        player_rect = patches.rectangle((square.x + offset, square.y + offset), rel_size, rel_size,
                                        fill=True, color=player_cmap[square.owner],
                                        zorder=player_z_order, visible=True, label=square.owner)
        axis.add_patch(player_rect)

    axis.legend()
    # recalculate axis bounding boxes
    axis.autoscale_view()
    # force figure to draw
    axis.figure.canvas.draw()
    return axis
