from animal import Animal

def main():
    ani1 = Animal()
    ani2 = Animal("Rover", 2, "red", 60)
    # ani2.name = "Rover"
    # ani2.limb_count = 2
    # ani2.colour = "red"
    # ani2.energy = 60

    print(ani1.move("North"))
    print(ani1.eat("cake"))
    print(f"my energy level is {ani1.energy}")

    print(ani2.move("South"))
    print(ani2.eat("banana"))
    print(f"my energy level is {ani2.energy}")


if __name__ == '__main__':
    main()