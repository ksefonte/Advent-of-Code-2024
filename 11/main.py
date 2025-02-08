from collections import defaultdict

def read_file(file_path: str) -> list:
    file_out = []
    with open(file_path, 'r') as file:
        # file_lines = file.readlines()[0].split(" ")
        stones = [int(stone) for stone in file.readlines()[0].split(" ")]
    return stones

def read_into_dict(file_path: str) -> list:
    with open(file_path, 'r') as file:
        # file_lines = file.readlines()[0].split(" ")
        stones = defaultdict(int)
        for stone in file.readlines()[0].split(" "):
            stone = int(stone)
            stones[stone] += 1
    return stones

file = read_file("./input.txt")
fild = read_into_dict("./input.txt")
print(fild)

def plog(*input):
    #print(input)
    return

def dict_stone(stone: int, stones: dict) -> list:
    if stone == 0:
        plog("Zero found")
        stones[1] += 1
        stones[0] -= 1
    elif len(str(stone)) % 2 == 0:
        plog("Even stone found")
        half_index = int(len(str(stone))/2)
        plog(half_index)
        stone_left = str(stone)[:half_index]
        stone_right = str(stone)[half_index:]
        stones[stone_left] +=1
        stones[stone_right] +=1
    else:
        plog("No previous rules apply, 2024ifying")
        stones[stone * 2024] += 1

def process_stone(stone: int) -> list:
    if stone == 0:
        plog("Zero found")
        stone = 1
    elif len(str(stone)) % 2 == 0:
        plog("Even stone found")
        half_index = int(len(str(stone))/2)
        plog(half_index)
        stone_left = str(stone)[:half_index]
        stone_right = str(stone)[half_index:]
        plog(stone_left,stone_right)
        stone = int(stone_left),int(stone_right)
        return stone
    else:
        plog("No previous rules apply, 2024ifying")
        stone = stone * 2024
    return stone

def process_stones(
        stones: dict,
        iterations: int=1
    ) -> list:
    plog('full list:')
    plog(stones)
    stones_temp = {}
    for stone, count in stones.items():
        processed_stone = process_stone(stone)
        if isinstance(processed_stone,int):
            print("stone,count,stones_temp")
            print(stone,count)
            stones_temp[processed_stone] = stones_temp.get(processed_stone,0) + count
        elif isinstance(processed_stone,tuple):
            for stone_tup in processed_stone:
                stones_temp[int(stone_tup)] = stones_temp.get(int(stone_tup),0) + count
    plog(f"Pre it: {iterations}")
    plog(iterations)
    if iterations > 0:
        iterations -= 1
        stones = stones_temp
        process_stones(stones, iterations)
    elif iterations == 0:
        sum = 0
        for stone, count in stones.items():
            sum+=count
        print(sum)
        return stones_temp
    
def process_pebbles(
        stones: list,
        iterations: int=1
    ) -> list:
    stonesed_stones = []
    plog('full list:')
    plog(stones)
    for stone in stones:
        plog(f"Stone is: {stone}")
        if stone == 0:
            plog("Zero found")
            stone = 1
            stonesed_stones.append(stone)
        elif len(str(stone)) % 2 == 0:
            plog("Even stone found")
            half_index = int(len(str(stone))/2)
            plog(half_index)
            stone_left = str(stone)[:half_index]
            stone_right = str(stone)[half_index:]
            plog(stone_left,stone_right)
            stonesed_stones.append(int(stone_left))
            stonesed_stones.append(int(stone_right))
        else:
            plog("No previous rules apply, 2024ifying")
            stone = stone * 2024
            stonesed_stones.append(stone)
    plog(f"Pre it: {iterations}")
    iterations -= 1
    plog(iterations)
    plog(stonesed_stones)
    if iterations > 0:
        process_pebbles(stonesed_stones, iterations)
    else:
        print("length")
        print(len(stonesed_stones))
        return stonesed_stones


output = process_stones(fild,75)
print("Finished...")
print(output)