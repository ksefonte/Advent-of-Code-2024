import itertools as itt

def plog(*input):
    #print(input)
    return

with open("./input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    for index, line in enumerate(lines):
        lines[index] = [*line.strip()]


def map_grid(power_grid: list) -> list:
    py = len(power_grid)
    px = len(power_grid[0])
    characters = []
    mapped_coords = []
    for i in range(len(power_grid)):
        line = (power_grid[i])
        plog(len(line))
        for j in range(len(line)):
            contents = line[j]
            mapped_coords.append((j,i,contents,[]))
            if contents != '.': characters.append(contents)
    return mapped_coords,px,py, set(characters)

def generate_antennae_pairs(mapped_grid: list, character) -> list:
    antennae_pairs = []
    for coord in mapped_grid:
        x,y,unit,ant = coord
        if unit == character:
            antennae_pairs.append((x,y))
            plog(coord)
    pairs = itt.permutations(antennae_pairs,2)
    plog("Pre:")
    plog(antennae_pairs)
    antennae_pairs = []
    for pair in pairs:
            antennae_pairs.append(pair)
    plog(antennae_pairs)
    return antennae_pairs

def process_antennae_pairs(mapped_grid: list,character: str) -> list:
    antennae_pairs = generate_antennae_pairs(mapped_grid,character)
    output = []
    for pair in antennae_pairs:
        plog("Pair:")
        plog(pair)
        i = pair[0]
        j = pair[1]
        dx = i[0] - j[0]
        dy = i[1] - j[1]
        plog(i,j,dx,dy)
        a = (tuple(x + y for x,y in zip(i, (dx,dy))))
        b = (tuple(x - y for x,y in zip(j, (dx,dy))))
        if (0 <= a[0] < px and 0 <= a[1] < py):
            output.append(a)
        if (0 <= b[0] < px and 0 <= b[1] < py):
            output.append(b)
    print(character, 'output:', output)
    print(character, 'output len',len(set(output)))
    return output

def process_characters(mapped_grid: list, characters: list):
    nodes = []
    for character in characters:
        nodes += process_antennae_pairs(mapped_grid,character)
    nodes = list(dict.fromkeys(nodes))
    print("Nodes:",nodes)
    print(len(nodes))
    return nodes


mapped_grid,px,py,characters = map_grid(lines)
processed_characters = process_characters(mapped_grid,characters)