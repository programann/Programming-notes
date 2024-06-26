class HumanBeing:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height


bob = HumanBeing('Bob',25,'Male')
bob.name = 'Bobby'
print(bob)

