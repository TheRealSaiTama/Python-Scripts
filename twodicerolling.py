import random 

def randompick():
    return random.randint(1,6)

def main():
    dice1 = randompick()
    dice2 = randompick()
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")
    again = input("Roll again? (y/n): ")
    if again == "y":
        main()
    else:
        print("Bye!")

if __name__ == "__main__":
    main()
