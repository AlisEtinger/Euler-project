#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


# In[1]:


a = list (range(0, 1000, 3))
b = list (range(0, 1000, 5))
print (sum(a) + sum(b))


# In[ ]:




