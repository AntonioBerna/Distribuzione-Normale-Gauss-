import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

class GaussPlot:
    def __init__(self, mu=0, sigma=1, x_range=(-5, 5)):
        self.mu = mu
        self.sigma = sigma
        self.x_range = x_range
        self.x = np.linspace(*x_range, 1000)
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.25)
        self.line, = self.ax.plot(self.x, self.gauss(self.x))
        self.ax.set_ylim([0, 0.5])
        self.ax.grid()
        self.ax_mu = plt.axes([0.1, 0.1, 0.8, 0.03])
        self.ax_sigma = plt.axes([0.1, 0.15, 0.8, 0.03])
        self.slider_mu = Slider(self.ax_mu, 'Media', -3, 3, valinit=self.mu)
        self.slider_sigma = Slider(self.ax_sigma, 'Varianza', 0.1, 3, valinit=self.sigma)
        self.slider_mu.on_changed(self.update)
        self.slider_sigma.on_changed(self.update)

    def gauss(self, x):
        return np.exp(-(x - self.mu)**2 / (2 * self.sigma**2)) / (self.sigma * np.sqrt(2 * np.pi))

    def update(self, val):
        self.mu = self.slider_mu.val
        self.sigma = self.slider_sigma.val
        y = self.gauss(self.x)
        self.line.set_ydata(y)
        self.ax.set_ylim([0, max(y) * 1.1])
        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()

if __name__ == "__main__":
    gauss_plot = GaussPlot()
    gauss_plot.show()