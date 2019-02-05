#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_pizza(size,*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings：")
    for topping in toppings:
        print('- ' + topping)

my_pizza = make_pizza(16,'cheese')
print(my_pizza)



#%%
