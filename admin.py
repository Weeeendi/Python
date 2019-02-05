#!/usr/bin/env python
# coding: utf-8


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

        
class Admin():
    def __init__(self):
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can detele post','can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("The privilege " + privilege + '.')






