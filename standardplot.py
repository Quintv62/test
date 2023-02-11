import matplotlib.pyplot as plt
import numpy as np
y = np.linspace(0,20,5)
x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
XX, YY = np.meshgrid(x,y)
plt.plot(x,np.sin(x))
#new comment

#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot


