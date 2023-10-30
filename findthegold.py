import random 

def print_map(p_map):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["0","0","0"],["0","0","0"],["0","0","0"]]

gold_horizontal = random.randint(0,2)
gold_vertical = random.randint(0,2)
map1[gold_horizontal][gold_vertical] = "S"
gold_position = str(gold_horizontal) + str(gold_vertical)

position = input("Where do you want to put the gold?: ")

if position == gold_position:
    print("You found the gold!")
else:
    print("You didn't find the gold!")
    horizontal = int(position[0])
    vertical = int(position[1])
    map1[horizontal-1][vertical-1] = "X"
print_map(map1)

