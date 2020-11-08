# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:40:32 2020

@author: Donny
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# x = np.arange(0, 6, 0.1)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()

# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title('sine & cos')
# plt.legend()
# plt.show()

img = imread('./dataset/lena.png')
plt.imshow(img)
plt.show()