from animal import Animal
from elephant import Elephant


def main():
    ani1 = Animal()
    ani2 = Animal("Rover", 2, "red")
    # ani2.name = "Rover"
    ani2.limb_count = -1
    #ani2.set_limb_count(-2)
    #print(f"ani2's limb count is {ani2.get_limb_count()}")
    print(f"ani2's limb count is {ani2.limb_count}")
    # ani2.colour = "red"
    # ani2.energy = 60

    print(ani1.move("North"))
    print(ani1.eat("cake"))
    #print(f"my energy level is {ani1.energy}")

    print(ani2.move("South"))
    print(ani2.eat("banana"))
    #print(f"my energy level is {ani2.energy}")

    ele = Elephant("Nelly", 5, "Grey", 2.3)
    print(ele.move("North"))
    print(ele.spray_water())


if __name__ == '__main__':
    main()