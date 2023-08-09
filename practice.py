import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# used for plotting the graph 
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.show()


# commands used : pip3 install numpy matplotlib ,
# to use vertial enviroment : python3 -m venv venv and then source venv/bin/activate (to activate it )