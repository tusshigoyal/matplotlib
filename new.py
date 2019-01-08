#!usr/bin/env python3
import matplotlib.pyplot as plt

from matplotlib import style 

style.use("ggplot")
x=[5,8,10]
y=[12,6,19]
x1=[8,17,4]
y1=[15,6,22]
plt.grid(c="green")
plt.plot(x,y,marker="*",linewidth=5,label="firstline")
plt.plot(x1,y1,marker="X",linewidth=5,label="secondline")
plt.legend()#used to show labels
plt.title("Graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


