#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input('Введите число a= '))
b = int(input('Введите число b= '))
c = int(input('Введите число c= '))
import math
D=b**2-4*a*c
if D>0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)
    print(f'x1 =', x1)
    print(f'x2 =', x2)
elif D==0:
    x = (-b) / (2*a)
    print(f'x =', x)
else:
    print('Решений нет')


# In[ ]:




