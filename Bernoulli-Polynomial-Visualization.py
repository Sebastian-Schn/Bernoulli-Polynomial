import math
import numpy as np
from operator import add
import matplotlib.pyplot as plt


def B(n):
    if n == 0:
        return 1
    elif n == 1:
        return - 0.5
    else:
        s = 0
        for k in range(0,n):
            s += math.comb(n-1, k)* B(k) / (n-k+1)
        s *= n    
        return(s)
            


def B_poly(n, x):
    s = np.repeat(0,100)
    for k in range(0,n+1):
        s = s + math.comb(n,k)* B(k)* x**(n-k)
    return(s)





x = np.linspace(0,1,100)

for i in range(1,6):
    plt.plot(x, B_poly(i,x), label=r'B_' + str(i) + '(x)')
plt.legend()
plt.ylim(-0.2,0.2)
plt.title('Bernoullipolynome von Grad \$i = 1,...5\$')
plt.savefig("BP.pdf", format="pdf")
