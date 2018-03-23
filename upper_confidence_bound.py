# Upper Confidence Bound # алгоритм мы пишем сами

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
# даны 10ка строк, каждая строка - это новый пользователь
# которому показывают одну из 10 видов рекламы
# если у юзера стоит 1 напротив 3-го вида рекламы, а везде в других 0
# то пользователь нажмет только на 3-ий вид рекламы (2 индекс в python)
# если другие виды рекламы, то он не нажмет никуда больше, кроме как 3 вид
# получается у нас есть уже готовые результаты предсказаний и мы смотрим
# как алгоритм будет выбирать какой вид рекламы лучше показывать юзерам

# Implementing UCB
# step 1
import math
N = 10000 # количество пользователей
d = 10 # количество версий рекламы
ads_selected = [] # выбор рекламы на каждом шаге
numbers_of_selections = [0] * d # читерский метод создания вектора [0,0,0...]
sums_of_rewards = [0] * d

# step 2
for n in range(0, N) : # [0,10000)
  max_upper_bound = 0 # максимальная граница рекламы максимальной
  ad = 0 # индекс максимальной рекламы
  for i in range(0, d) :
    if (numbers_of_selections[i] > 0) :
      average_reward = sums_of_rewards[i] / numbers_of_selections[i]
      delta_i = math.sqet(3/2 * math.log(n + 1) / number_of_selections[i])
      upper_bound = average_reward + delta_i
    else :
      upper_bound = 1e400 # max item
    if (upper_bound > max_upper_bound) :
      max_upper_bound = upper_bound
      ad = i























