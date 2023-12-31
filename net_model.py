# -*- coding: utf-8 -*-
"""net_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AOED8p1KTmceelxhJoyGTE-P4DjXp3T0
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

def get_net():
  class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)#первые ядра -палочки, с каждым слорем усложнение форм, комбтнация предыдущих
        #снчаала колво каналов,потом длина ширина у изображения
        #conv 1 - колво каналов 2 - колво признкаов вывходных(ядро)б  3 - если квадратное - сторона квадрата размер ядра или(1,2) обычно 3 квадрат
        #stride - смещенеи на n пикселйе если 1 - с каждой стороны на 1 пиксель меньше
        #padding - заполнение рамки размера n нулями, обычно такой чтобы изображения совпадало с исходным
        #dilation - расстояние между клетками ядра
        #groups - глубина ядра
        #(3,32,32)->(6,28,28)->(16, 24, 24)
        self.pool = nn.MaxPool2d(2, 2)#
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)# to vector
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))#
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
  net = Net()
  return net