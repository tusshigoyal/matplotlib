#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[20]:


x=[4,7,9,12]
y=[3,6,9,2]



# In[22]:
matplotlib.use('TkAgg')
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []

plt.xlabel('distance')
plt.ylabel('time')
plt.grid(c='green')
plt.plot(x,y)  #to plot graph in maths way
plt.bar(x,y)
plt.bar(y,x)
plt.show() # to show plot


# In[ ]:




