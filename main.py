import numpy
import matplotlib.pyplot as plt


#Scatter Plot
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

x_2 = numpy.random.normal(5.0, 1.0, 1000)
y_2 = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x_2, y_2)
plt.show()