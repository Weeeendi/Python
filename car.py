#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

