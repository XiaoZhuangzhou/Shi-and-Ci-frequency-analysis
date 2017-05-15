import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
def draw_bar(num,name):
  x = range(len(num))
  xticks=name
  plt.bar(x, num, alpha = .5, color = 'g',width=0.5)
  plt.xticks(x,xticks,size='small',rotation=30)
  plt.show()