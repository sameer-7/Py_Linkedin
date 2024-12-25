# Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python. It is highly customizable and widely used for visualizing data.
import matplotlib.pyplot as plt
#sample data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

#creating a line plot
plt.plot(x,y,marker = 'o')
plt.title("Line plot example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()