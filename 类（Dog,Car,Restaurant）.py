#!/usr/bin/env python
# coding: utf-8

# # 类

# ## 创建和使用类 

# 与C++的类雷同，都是面向对象编程

# ### 创建Dog类

# In[8]:


#dog.py

class Dog():
    """The attempt to simulate a puppy"""
    
    def __init__(self,name,age):
        """Initialization function"""
        self.name = name
        self.age =age
        
    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " is now rolling over.")


# ### 根据类创建实例

# In[15]:


my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old.')


# In[17]:


my_dog.sit()
my_dog.roll_over()


# In[18]:


your_dog = Dog("lucy",3)


# In[19]:


your_dog.sit()


# ### trying

# In[28]:


class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def incretment_number(self,numbers):
        if self.number_served + numbers < 0:
            print("The number of guests is wrong!")
        else:
            self.number_served += numbers
    
    def set_number_served(self):
        print("At present, the number of people eating in the restaurant is: " + str(self.number_served))
        
    def describe_restaurant(self):
        print("It's a " + self.type + " restuarant named " + self.name + '.')
    


# In[30]:


New_restaurant = Restaurant("Blue","beef noodle")
New_restaurant.incretment_number(20)
#New_restaurant.incretment_number(-30)
New_restaurant.describe_restaurant()
New_restaurant.set_number_served()


# ## 使用类和实例

# ### Car.py

# In[4]:


class Car():
    """一次模拟汽车的简单测试"""
    
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_desciptive_name(self):
        """return the clearly desciptive message"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi','A6',2010)
print(my_new_car.get_desciptive_name())


# ### 给属性指定默认值

# In[21]:


class Car():
    """一次模拟汽车的简单测试"""
    
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
        
    def get_desciptive_name(self):
        """return the clearly desciptive message"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print("This car has " + str(self.odometer_reading) + " mile on it.")
        
    def update_odometer(self,milage):
        """将里程表读数设置为指定的值"""
        """禁止将里程表读数进行回调"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the odometer!")
    
    def increment_odometer(self,miles):
        if miles < 0:
            print("You can't roll back the odometer!")
        else:
            self.odometer_reading += miles
    
my_new_car = Car('audi','A6',2010)
print(my_new_car.get_desciptive_name())
my_new_car.read_odometer()


# ### 修改属性的值 

# #### 1.直接修改属性值

# In[22]:


my_new_car = Car('audi','A6',2010)
print(my_new_car.get_desciptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# #### 2.通过方法修改属性的值

# In[23]:


my_new_car.update_odometer(16)
my_new_car.read_odometer()


# >可对方法update_odometer()进行扩展，使其在修改里程表读数是做些额外得工作，比如禁止任何人将表里的里程读数进行回调
# 

# In[24]:


my_new_car.update_odometer(10)


# #### 3.通过方法对属性值进行递增 

# In[25]:


my_new_car.increment_odometer(2500)
my_new_car.read_odometer()


# ## trying

# In[34]:


class User():
    """记录客户的姓名即其他基本信息"""
    def __init__(self,frist_name,last_name,gender,age):
        self.frist_name = frist_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0
        
    def descirptive_user(self):
        formatted_name = self.frist_name + ' ' + self.last_name
        print("Formatted_name: " + formatted_name +
             "\tGender: " + self.gender +
             "\tAge: " + str(self.age))
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def check_login_attempts(self):
        print("The number of user logins ：" + str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
Guest1 = User('David','Brewn','female',24)
Guest1.descirptive_user()
Guest1.increment_login_attempts()
Guest1.check_login_attempts()
Guest1.reset_login_attempts()
Guest1.check_login_attempts()


# In[ ]:




