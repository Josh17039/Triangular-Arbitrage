import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8.878*((np.exp((x)/(222.875*0.025)))-1)

vlist = np.arange(0,1.1,0.1)

ilist = f(vlist)

plt.figure(num=0,dpi=120)
plt.plot(vlist,ilist)
