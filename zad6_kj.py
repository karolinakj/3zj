#Zadanie 6: Podaj maksymalną wartość w każdym wierszu poniższej tablicy

import numpy as np
np.random.seed(100)
m = np.random.randint(20, size=[5,5])
m
print(m)
print("----")

max_wiersz =np.amax(m,axis=-1)
print(max_wiersz)