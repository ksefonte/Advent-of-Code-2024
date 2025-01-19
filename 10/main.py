def get_list_element(lines,y,x):
    return "" if x < 0 or y < 0 or y >= len(lines) or x >= len(lines[y]) else lines[y][x]

def get_neighbours(lines,y,x):
    print("Neighbours:")
    # print(lines)
    return (
        (y-1, x,get_list_element(lines,y-1,x)), ##T
        (y,x+1,get_list_element(lines,y,x+1)), ##R
        (y+1,x,get_list_element(lines,y+1,x)), ##B
        (y,x-1,get_list_element(lines,y,x-1))   ##L
    )
    # match dir:
    #     case "top":
    #         return (y-1, x,get_list_element(lines,x,y-1))
    #     case "right":
    #         return (y, x+1,get_list_element(lines,x+1,y))
    #     case "bot":
    #         return (y+1, x,get_list_element(lines,x,y+1))
    #     case "left":
    #         return (y,x-1,get_list_element(lines,x-1,y))
    #     case _:
    #         return None

def find_trail(lines,y,x,current,trail=None,trails=None):
    if trail is None:
        trail = [(y,x,current)]
    if trails is None:
        trails = []
    print("Finding...")
    (top,right,bot,left) = get_neighbours(lines,y,x)
    print(f"t{top} r{right} b{bot} l{left} : {trail}")
    for neighbour in top,right,bot,left:
        if neighbour[2] == 9 and current == 8:
            print("Found 9, appending")
            trail.append(neighbour)
            print(trail)
            trails.append(trail)
            print("Trails:")
            print(trails)
            trail = []
            return trails
        elif neighbour[2] == current+1:
            if neighbour not in trail:
                trail.append(neighbour)
                print(f"Consecutive neighbour found {neighbour}")
                find_trail(lines, neighbour[0], neighbour[1], neighbour[2], trail)
        else:
            print(f"Trail ended at x,y: {x,y}")
    return trails        

with open("./test.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    for index, line in enumerate(lines):
        lines[index] = [int(num) for num in line]

total = 0

trailheads = []
trailhead = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        trail = []
        if get_list_element(lines,x,y) == 1:
            print(F"Found 1 at {y,x}")
        trails = (find_trail(lines,y,x,1))
        if trails:
            print("Trail is:")
            print(trails)
