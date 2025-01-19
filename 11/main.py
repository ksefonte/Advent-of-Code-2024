def read_file(file_path: str) -> list:
    file_out = []
    with open(file_path, 'r') as file:
        # file_lines = file.readlines()[0].split(" ")
        stones = [int(stone) for stone in file.readlines()[0].split(" ")]
    return stones

file = read_file("./test2.txt")

def process_stones(
        stones: list,
        iterations: int=1
    ) -> list:
    stonesed_stones = []
    print('full list:')
    print(stones)
    for stone in stones:
        print(f"Stone is: {stone}")
        if stone == 0:
            print("Zero found")
            stone = 1
            stonesed_stones.append(stone)
        elif len(str(stone)) % 2 == 0:
            print("Even stone found")
            half_index = int(len(str(stone))/2)
            print(half_index)
            stone_left = str(stone)[:half_index]
            stone_right = str(stone)[half_index:]
            print(stone_left,stone_right)
            stonesed_stones.append(int(stone_left))
            stonesed_stones.append(int(stone_right))
        else:
            print("No previous rules apply, 2024ifying")
            stone = stone * 2024
            stonesed_stones.append(stone)
    print(f"Pre it: {iterations}")
    iterations -= 1
    print(iterations)
    print(stonesed_stones)
    if iterations > 0:
        process_stones(stonesed_stones, iterations)
    else:
        print("length")
        print(len(stonesed_stones))
        return stonesed_stones


output = process_stones(file,25)