import random 

string = input("Input everyone's name, separated by a comma: ")
names = string.split(",")

def randompick():
    return random.randint(0,len(names)-1)

def main():
    print(f"{names[randompick()]} will pay the bill today!")

if __name__ == "__main__":
    main()