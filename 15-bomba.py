'''Contagem regressiva de uma bomba'''

import numpy as np
import time

print("Iniciando contagem regressiva:")

for segundos in range (10, -1, -1):
    print("Restam: ", segundos, "segundos para a bomba explodir")
    time.sleep(1)
    if (segundos == 0):
        print("BUM!")