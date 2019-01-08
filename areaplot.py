#!usr/bin/env python3
import matplotlib.pyplot as plt
days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[9,8,7,4,4]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label="sleeping",linewidth=5)
plt.plot([],[],color='g',label="eating",linewidth=5)
plt.plot([],[],color='r',label="working",linewidth=5)
plt.plot([],[],color='k',label="playing",linewidth=5)
#m=magenta,k=black
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','g','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title("Stack Plot / Area plot")
plt.legend()# used to show label
plt.show()

