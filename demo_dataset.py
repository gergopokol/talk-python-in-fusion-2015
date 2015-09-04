"""
EXCERSISE: Let's illustrate the effect of heating on the electron
           density/temperature profiles.
"""

import matplotlib.pyplot as plt
import xray

from demo_working_environment import highlight_x


def plot_scope(ax, da):
    ax.plot(da['time'], da, label=da.name)
    ax.set_xlabel('time [s]')
    ax.legend()


def plot_profile(ax, da, time):
    lines = ax.plot(da['rho'], da.sel(time=time, method='nearest'))
    ax.set_xlabel(r'$\rho_\mathrm{tor}$')

    for line, tim in zip(lines, time):
        line.set_label('{}@{} s'.format(da.name, tim))

    ax.legend(loc='best')


ds = xray.open_dataset('dataset/pr98_jet_19649.nc')
times = [45, 47]

# Prepare the figure and the axes
fig = plt.figure(1)
fig.clf()

ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

# Create the plots
plot_profile(ax1, ds['ne'], time=times)

plot_profile(ax2, ds['te'], time=times)
plot_profile(ax2, ds['ti'], time=times)

plot_scope(ax3, ds['pnbi'])

for t in times:
    highlight_x(ax3, (t - 0.05, t + 0.05))

# Matplotlib boilerplate
plt.tight_layout()
plt.draw()
plt.show()
