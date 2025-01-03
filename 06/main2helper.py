import copy


"""https://www.youtube.com/watch?v=b0R9_DFKFEU"""
## Copped out of day 2 using solution online.
## TODO: Finish using original approach

def get_list_element(lines, x, y):
    return "" if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]) else lines[x][y]

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    for index, line in enumerate(lines):
        lines[index] = [*line]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if get_list_element(lines,y,x) == '^':
            ystart = y
            xstart = x
            break
directions = [[-1,0],[0,+1],[+1,0],[0,-1]]

total = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        direction = 0
        if get_list_element(lines, y, x) == '.':
            lines[y][x] = '#'
            current = [ystart, xstart, 0]
            places = set(tuple([ystart, xstart, 0]))
            while get_list_element(lines, current[0], current[1]) != "":
                dy = current[0] + directions[direction][0]
                dx = current[1] + directions[direction][1]
                if get_list_element(lines, dy, dx) in ['.', '', '^']:
                    if tuple([dy, dx, direction]) not in places:
                        places.add(tuple([dy, dx, direction]))
                        current = [dy, dx, direction]
                    else:
                        total +=1
                        print(f"Success at {str(y)} and {str(x)}")
                        break
                elif get_list_element(lines, dy, dx) == '#':
                    direction = (direction + 1) % 4
            lines[y][x] = '.'

print(f"Total: {total}")