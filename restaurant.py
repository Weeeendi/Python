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