#!/usr/bin/env python
# coding: utf-8

# In[1]:


unconfirmed_users = ['alice','brain','candace']
confirmed_users=[]

#验证每个用户，直到没有需要验证的用户为止
#将每个经过验证的列表都移到已验证用户列表当中

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
#显示每个用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    


# In[5]:


pets = ['dog','cat' ,'dog','goldfish','cat','rabbit','cat']
print(pets)

while "cat" in pets:
    pets.remove('cat')
    
print("\n")
print(pets)


# In[8]:


sandwich_orders = ['standard ','cheese','potato']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your tuna sandwich:"+finished_sandwich)
    finished_sandwiches.append(finished_sandwich)
    
print("\nThe following list is which have been finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)


# In[10]:


for i in range(1,4):
    finished_sandwiches.append('pastrami')

print(finished_sandwiches)
print("\nThe patrami sandwich has been saled out!" )
while "pastrami" in finished_sandwiches:
    finished_sandwiches.remove("pastrami")

print(finished_sandwiches)


# In[13]:


wishing_place = {}
#退出标志
polling_active = True

while polling_active:
    residence = input("Where are you residenting now ? ")
    place = input("If you could visit one place in the world, where would you go?")
    wishing_place[residence] = place
    
    repeat = input("Would you like to anothor person repond?(yes/no)")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for resident,place in wishing_place.items():
    print("\n现居地："+resident.title())
    print("最想去的地方："+place.title())
    


# In[ ]:




