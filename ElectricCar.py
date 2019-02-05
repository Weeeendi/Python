#!/usr/bin/env python
# coding: utf-8

# ## 1.子类的方法__init __( )

# 下面创建一个简单的ElectricCar类版本，它具有Car的全部功能

# ### electric_car.py

# In[27]:


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
    
    def fill_gas_tank(self):
        print("This car's gas tank is full.")

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) +  "-KWh battery.")
        
    def get_range(self):
        """display the range mileage of battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " mlies on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        #将实例用作属性
        self.battery = Battery()
        """对父类中的fill_gas_tank进行重写"""
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank.")
        """       
        self.battery_size = 70
        添加了新属性self.battery_size        
    def describe_battery(self): 
        打印一条电池描述信息
        print("This car has a " + str(self.battery_size) +  "-KWh battery.")
        """        
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_desciptive_name())
my_tesla.battery.describe_battery()

# ## 2.给子类定义属性和方法

# 让一个类继承另一个类后，可添加区分子类和父类所需的属性和方法

# In[4]:





# ## 3.重写父类的方法

#     如果有人调用fill_gas_tank(),python将忽略Car类中的方法fill_gas_tank（）

# In[6]:


my_tesla.fill_gas_tank()


# ## 4.将实例用作属性

# In[22]:





# In[20]:


my_tesla.battery.describe_battery()


# 这看似做了很多额外的工作，但保证了ElectricCar类的整洁性，我们只需要详细的描述Battery的属性即可

# In[26]:


my_tesla.battery.get_range()


# ## 5.模拟实物

# 在模拟比较复杂的对象时，我们需要解决一些问题。比如上面的例子里，我们要将get_range()放在Car类里还是battery类中

# 如果描述一俩车时放在battery类中也许是合适的，但如果描述的是一条汽车生产线中我们最好将其放在ElectricCar中，当然我们也可以这么做，依然将get_range放在battery中，但向他传递一个参数Car_model,根据不同的型号来判断汽车的里程

# It is not has right or wrong when you set up model for the real life things,there are some methods have more efficiency，but if you want to find the most efficient method should go through some practice.

# ## trying

# The ice-cream shop
# > 编写一个名为IceCreamStand的类，继承restaurant类，并添加一个名为flavours的属性，用于储备一个由各种口味冰激凌组成的列表，创建一个名为IceCreamStand的实例，并调用这个方法。

# In[32]:


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
        
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate','melon','Strawberry']
    
IceCream_shop = IceCreamStand('Queen','iceCream')
for Icecream in IceCream_shop.flavors:
    print("The " + Icecream + "-flavored ice-cream sale on here.")
        


# In[35]:


class Admin():
    def __init__(self):
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can detele post','can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("The privilege " + privilege + '.')
            
Admin1 = Admin()
Admin1.privileges.show_privileges()


# In[ ]:




