import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [u'SimHei']

xnum = [16,  14,  12, 9, 10,9]
x = range(len(xnum))
for i in x:
  xnum[i]/=12367#归一化
ynum= [856,  1103,  763, 717,  668,559]
y = range(len(ynum))
for i in y:
  ynum[i] /= 523123*1.5#归一化
xticks=['明月',  '春风',  '故人',  '长安',  '白日','天子']
plt.bar(x, xnum, alpha = .2, color = 'b',width=0.5,label="唐诗三百首")#draw a bar
plt.bar(y, ynum, alpha = .2, color = 'r',width=0.5,label="唐诗四万首")
plt.xticks(x, xticks, size='small', rotation=30)
plt.legend(loc='upper right')
plt.show()
