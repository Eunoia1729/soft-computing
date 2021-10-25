
"""
## Question 1: Create Datasets
"""

import numpy as np

n_dataset = 15
n_class = 10
n_class_size = 20

def checkSampleVariance():
  population = np.random.randint(1,100,200)
  for i in range(n_class):
    pop_class = population[n_class*i:n_class*(i + 1)]
    print(f'class {i}:')
    print(f'mean : {np.mean(pop_class)}')
    print(f'variance : {np.var(pop_class)}')
  print(f'Population mean : {np.mean(population)}')
  print(f'Population variance : {np.var(population)}')

for i in range(n_dataset):
  print(f"DATA SET {i + 1} : ")
  checkSampleVariance()
