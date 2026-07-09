class Animal:
    _limb_count:int = 0

    def __init__(self, name:str="Anon", limb_count:int=4, colour:str="Black"):
        self.name = name
        self._limb_count = limb_count
        self.colour = colour
        self._energy = 50

    def get_limb_count(self)->int:
        return self._limb_count

    def set_limb_count(self, value:int)->None:
        if value < 0:
            value = 0
        self._limb_count = value

    limb_count:int = property(get_limb_count, set_limb_count)

    def eat(self, food:str):
        self._energy += 5
        return (f"I'm an {self.colour} animal called {self.name} "
                f"using some of my {self._limb_count} limbs to eat {food}")

    def move(self, direction:str):
        self._energy -= 1

        return (f"I'm an {self.colour} animal called {self.name} "
                f"using some of my {self._limb_count} limbs to move {direction}")