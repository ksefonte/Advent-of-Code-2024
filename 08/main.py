import itertools as itt
import math as Math

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
    plog(character, 'output:', output)
    print(character, 'output len',len(set(output)))
    return output

def process_sprawling_pairs(mapped_grid: list,character: str) -> list:
    antennae_pairs = generate_antennae_pairs(mapped_grid,character)
    output = []
    print(f"Processing {character}")
    for pair in antennae_pairs:
        plog("Pair:")
        plog(pair)
        i = pair[0]
        j = pair[1]
        dx = i[0] - j[0]   
        dy = i[1] - j[1]
        # print(i,j,dx,dy)
        plog("Root is:",i)
        if len(i) > 1:
            print(i)
            output.append(i)
        if len(j) > 1:
            print(j)
            output.append(j)
        plog(f"px {px} - i[0] {i[0]} div {dx}")
        plog(f"py {py} - i[1] {i[1]} div {dy}")
        iterxypos = min(
            Math.floor(abs(((px-i[0]) / dx))),
            Math.floor(abs((py-i[1]) / dy))
            )
        iterxyneg = min(
            abs(Math.floor((i[0]) / dx)),
            abs(Math.floor((i[1]) / dy))
            )
        plog(f"iterations dx dy {dx, dy}")
        print(f"Antennae pair {character} {i,j} Gradient: {dx,dy} Number of iterations to edge: p{iterxypos} or n{iterxyneg} {py, px}")
        for iter in range(px):
            a = (tuple(x + y for x,y in zip(i, (dx*(iter+1),dy*(iter+1)))))
            if (0 <= a[0] < px and 0 <= a[1] < py):
                print("ap",pair[0],a)
                output.append(a)
            c = (tuple(x - y for x,y in zip(i, (dx*(iter+1),dy*(iter+1)))))
            if (0 <= c[0] < px and 0 <= c[1] < py):
                print("cp",pair[0],c)
                output.append(c)
            b = (tuple(x + y for x,y in zip(i, (dx*(iter+1),dy*(iter+1)))))
            if (0 <= b[0] < px and 0 <= b[1] < py):
                print("bn",pair[0],b)
                output.append(b)
            d = (tuple(x - y for x,y in zip(i, (dx*(iter+1),dy*(iter+1)))))
            if (0 <= d[0] < px and 0 <= d[1] < py):
                print("dn",pair[0],d)
                output.append(d)
        # b = (tuple(x - y for x,y in zip(j, (dx,dy))))
        # if (0 <= b[0] < px and 0 <= b[1] < py):
        #     print("b",pair[0],b)
        #     output.append(b)
    plog(character, 'output:', output)
    plog(character, 'output len',len(set(output)))
    return output

def process_characters(mapped_grid: list, characters: list):
    nodes = []
    for character in characters:
        processed_c = process_sprawling_pairs(mapped_grid,character)
        nodes += processed_c
        print(f"Processed: {character} x {len(processed_c)}")
    nodes = list(dict.fromkeys(nodes))
    print(len(characters),characters)
    # print("Nodes:",nodes)
    print(len(nodes))
    return nodes


mapped_grid,px,py,characters = map_grid(lines)
processed_characters = process_characters(mapped_grid,characters)