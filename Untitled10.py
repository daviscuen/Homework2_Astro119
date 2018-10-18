#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

print(np.arange(0, (2* np.pi), ((2* np.pi)/1000), dtype= float))


x = np.arange(0,2* np.pi, .01)
plt.xlim(0,2* np.pi)
plt.ylim(-1, 10)
y1 = 5.5* np.cos(2*x) + 5.5
y2 = 0.02 * np.exp(x)
y3 = (0.25* x**2 + (.1* np.sin(10*x)))
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xlabel("Time in Astro119")
plt.ylabel("Measure of Awesomeness")
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

print(np.arange(0, (2* np.pi), ((2* np.pi)/1000), dtype= float))


x = np.arange(0,2* np.pi, .01)
plt.xlim(0,2* np.pi)
plt.ylim(-1, 10)
y1 = 5.5* np.cos(2*x) + 5.5
y2 = 0.02 * np.exp(x)
y3 = (0.25* x**2 + (.1* np.sin(10*x)))
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xlabel("Time in Astro119")
plt.ylabel("Measure of Awesomeness")
plt.show()


# In[ ]:




