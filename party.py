#!/usr/bin/env python
# coding: utf-8

# In[1]:


#邀请5位亲朋好友来参加你的宴会
Guest_list=["Wen Runjun","Zhen Wenjuan","Wang Zhihao","Zhen Yidan","Zhen Dajiang"]


# In[2]:


#为每个人发送邀请
for Guest in Guest_list:
    print("Dear "+ Guest + ",I would like to invite you join the party")
#有一人无法出席,指出是谁无法赴约,将其该为另一位新嘉宾
print("I'm sorry for Wen Runjun's absence,and Wang Guiyang will attend to the party")
Guest_list[0]="Wang Guiyang"


# In[3]:


#有了更大的桌子,可以邀请更多的嘉宾参与
print("Now,I find a bigger table for my party,and we could invite more three new guests!")
Guest_list.insert(0,'KangQiao')
Guest_list.insert(3,'Li Wanling')
Guest_list.append("Zhao Zijie")
for Guest in Guest_list:
    print("Dear "+ Guest + ",I would like to invite you join the party")
print(Guest_list)


# In[4]:


#通知大家只能邀请2位出席宴会,将嘉宾人数缩减为两人
print("I'm sorry to tell you thar i can only invite two guests to dinner")
while len(Guest_list)>2:
    print("Dear "+Guest_list.pop()+",I'm sorry you can't attend the dinner party.")


# In[5]:


#通知仍在名单的嘉宾
for Guest in Guest_list:
    print(Guest + ",You still in the list of inviter")
    del Guest
    


# In[6]:


#删除剩余名单
del Guest_list[1]
del Guest_list[0]


# In[7]:


print(Guest_list)

