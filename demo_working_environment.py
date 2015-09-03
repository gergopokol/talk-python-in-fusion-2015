"""
1. Present working environment
    * matplotlib axes are good primitives to pass around (not figures)
    * separate content and apperance
        - see more Grammar of Graphics, ggplot http://ggplot.yhathq.com/
    * re-use 'plots' on other figures

2. Implement highlight_y and make_bw_friendly functions

"""

import numpy as np
import matplotlib.pyplot as plt


def plot_sin(ax):
    """ Plot a sine wave """
    x = np.linspace(0, 2 * np.pi, 100)

    for w in [1, 2, 4]:
        ax.plot(x, np.sin(w * x))

    ax.set_xlabel('time [s]')
    ax.set_ylabel('amplitude [m]')


def plot_sinc(ax):
    """ Plot the sinc function """
    x = np.linspace(-4, 4, 100)
    y = np.sinc(x)

    ax.plot(x, y)

    ax.set_xlabel('position [m]')
    ax.set_ylabel('amplitude [m]')


if plt.fignum_exists(1):
    plt.figure(1).clf()

fig, axes = plt.subplots(2, num=1)
plot_sin(axes[0])
plot_sinc(axes[1])

plt.tight_layout()
plt.draw()

# Let's reuse the plot_sinc function on a new figure
# fig2 = plt.figure(2)
# fig2.clf()
# ax = fig2.add_subplot(111)
# plot_sinc(ax)
# plt.tight_layout()
# plt.draw()


# def make_bw_friendly(ax):
#     """ Make the axis understandable on black and white print """
#     from itertools import cycle
#
#     linewidth = 2
#     color = 'black'
#     styles = ['-', '--', '-.', '.']
#
#     for line, style in zip(ax.lines, cycle(styles)):
#         line.set_linewidth(linewidth)
#         line.set_color(color)
#         line.set_linestyle(style)


# def highlight_y(ax, limits, **kwargs):
#     """ Highlight parts of the plot on the x-axis between range """
#     xmin, xmax = limits
#
#     # save the arguments internally
#     _kwargs = {}
#     _kwargs.update(kwargs)
#
#     # set default opacity for the overlay
#     if 'alpha' not in _kwargs:
#         _kwargs['alpha'] = 0.5
#
#     ax.axhspan(xmin, xmax, **_kwargs)


# highlight_y(axes[1], (0.2, 0.5), color='red')
# make_bw_friendly(axes[0])

plt.show()
