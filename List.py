#!/usr/bin/env python
# coding: utf-8

# In[1]:


for value in range(1,5):
    print(value)


# In[2]:


number = list(range(1,6))
print(number)


# In[3]:


even_number = list(range(2,11,2))
print(even_number)


# In[4]:


squares=[]
for value in range(1,11):
    square=value**2         #squares.append(value**2)
    squares.append(square)
    
print(squares)


# In[5]:


sum(squares)


# In[6]:


max(squares)


# In[7]:


min(squares)


# In[8]:


squares=[value**2 for value in range(1,11)]#等价于上面的代码
print(squares)


# In[9]:


number1=list(range(1,21))
print(number1)


# In[10]:


number2=list(range(1,1000001))
print(number2)


# In[13]:


number3=list(range(3,33,3))
print(number3)


# In[14]:


number_squares=[value**3 for value in range(1,11)]
print(number_squares)


# In[ ]:




