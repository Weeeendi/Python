from random import randint
x = randint(1,6)

class Die():
    def __init__(self,side=6):
        self.side = side

    def roll_die(self):
        print(randint(1,self.side))

side6 = Die(6)
side10 = Die(10)
side20 = Die(20)
for i in range(1,11):
    print('\n')
    side6.roll_die()
    side10.roll_die()
    side20.roll_die()
   