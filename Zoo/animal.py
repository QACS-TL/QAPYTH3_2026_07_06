class Animal:

    def __init__(self, name:str="Anon", limb_count:int=4, colour:str="Black", energy:int=50):
        self.name = name
        self.limb_count = limb_count
        self.colour = colour
        self.energy = energy

    def eat(self, food:str):
        self.energy += 5
        return (f"I'm an {self.colour} animal called {self.name} "
                f"using some of my {self.limb_count} limbs to eat {food}")

    def move(self, direction:str):
        self.energy -= 1
        return (f"I'm an {self.colour} animal called {self.name} "
                f"using some of my {self.limb_count} limbs to move {direction}")