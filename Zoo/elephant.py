from animal import Animal

class Elephant(Animal):
    trunk_length:float = 1.3

    def __init__(self, name:str="Anon", limb_count:int=4, colour:str="Black", trunk_length:float=1.3):
        super().__init__(name, limb_count, colour)
        self.trunk_length = trunk_length

    def spray_water(self):
        return f"I'm an elephant called {self.name} spraying water!"