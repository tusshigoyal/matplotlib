#!usr/bin/env python3
import matplotlib.pyplot as plt

year=[2000,2001,2002]
jan=[400,480,430]
feb=[318,342,391]
mar=[362,406,419]
apr=[348,396,461]
may=[363,420,472]
jun=[435,472,535]
jul=[491,548,622]


plt.plot([],[],color='m',label="jan",linewidth=3)
plt.plot([],[],color='b',label="feb",linewidth=3)
plt.plot([],[],color='g',label="mar",linewidth=3)
plt.plot([],[],color='r',label="apr",linewidth=3)
plt.plot([],[],color='y',label="may",linewidth=3)
plt.plot([],[],color='k',label="jun",linewidth=3)
plt.plot([],[],color='c',label="jul",linewidth=3)

plt.stackplot(year,jan,feb,mar,apr,may,jun,jul,colors=['m','b','g','r','y','k','c'])

plt.xlabel('year')
plt.ylabel('People')
plt.legend()
plt.title("Travel Info")
plt.show()
