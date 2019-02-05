#!/usr/bin/env python
# coding: utf-8

# In[8]:


cars = ['bmw','audi','toyota','subaru']


# In[4]:


cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


# In[5]:


#临时排序
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# In[9]:


cars.reverse()
print(cars)


# In[10]:


len(cars)


# In[26]:


place=["Japen","Gui Lin","ShangHai","Beijing","Maldives"]
print(place)


# In[27]:


print(sorted(place))


# In[28]:


print(sorted(place,reverse=True))


# In[29]:


print(place)


# In[30]:


place.reverse()
print(place)


# In[32]:


place.sort()
print(place)


# In[33]:


place.sort(reverse=True)
print(place)


# In[34]:


print(place[-1])


# In[35]:


while len(place)>=1:
    place.pop()


# In[ ]:




