import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from scipy.stats import norm
 
def Distribuzione_Normale(ax, dominio, micro, varianza):
    if varianza != 0.0:
        ax.plot(dominio, norm.pdf(dominio, micro, varianza))
    else:
        ax.cla()
 
# Aggiornamento Dati
def update(val):
    ax.cla()
    micro = s_micro.val
    varianza = s_varianza.val
    Distribuzione_Normale(ax, micro, varianza)
 
ax = plt.subplot(111)
plt.subplots_adjust(left=0.10, bottom=0.25)
 
# Posizionamento
ax_micro = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_varianza = plt.axes([0.25, 0.15, 0.65, 0.03])
 
# Variabili
micro_0 = 0.0
varianza_0 = 0.3  # La varianza è σ^2
dominio = np.linspace(-4, 4, 1000)
 
# Slider per micro e varianza
s_micro = Slider(ax_micro, "Valore atteso (μ): ", 0.0, 1.0, valinit=micro_0)
s_varianza = Slider(ax_varianza, "Varianza (σ^2): ", 0.0, 1.0, valinit=varianza_0)
s_micro.on_changed(update)
s_varianza.on_changed(update)
 
# Grafico Distribuzione Normale [Gaussiana]
Distribuzione_Normale(ax, dominio, micro_0, varianza_0)
plt.show()
