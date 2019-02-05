class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can detele post','can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("The privilege " + privilege + '.')