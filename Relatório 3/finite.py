#implentações de Diferenças Finitas

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
#%matplotlib inline




# step size
h = 0.7
# define grid
x = np.arange(0, 2*np.pi, h) 
# compute function
y = x**2+3

# compute vector of forward differences
forward_diff = np.diff(y)/h 
# compute corresponding grid
x_diff = x[:-1:] 
# compute exact solution
exact_solution = -np.sin(x_diff) 

# Compute max error between 
# numerical derivative and exact solution
max_error = max(abs(exact_solution - forward_diff))
print(max_error)

# Plot solution
plt.figure(figsize = (10, 6))
plt.plot(x_diff, forward_diff, '--', \
         label = 'Aproximação')
plt.plot(x_diff, exact_solution, \
         label = 'Solução Exata')
plt.xlabel("Max Error:" + str(max_error))
plt.legend()
plt.show()




