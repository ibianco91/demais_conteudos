import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import urllib
import datetime as dt
from matplotlib import style
from openpyxl import load_workbook


style.use('classic')

x = [1,2,3,4,5,6]
y = [100,200,300,400,400,300]

x2 = [2,3,9]
y2 = [350,680,500]

plt.plot(x,y, label='Primeira curva')  # marker ='x' entre virgulas
plt.plot(x2,y2, label ='Segunda curva')  # color ='blue' entre virgulas
plt.xlabel('Deformação axial (%)')  # titulo eixo X
plt.ylabel('Tensão Vertical (kPa)')  # titulo eixo Y
plt.title('Compressão não-confinada')  # titulo do gráfico


plt.legend()
plt.show()
