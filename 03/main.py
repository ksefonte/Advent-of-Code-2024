import re

def read_file(file_path: str) -> list:
    memory = ""
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            memory += (line)
    return memory

def split_memory_by_dodont(memory: str):
    print("=========================")
    do_action = []
    dont_action = []
    total_multipliers = []
    total_running_total = 0
    action_block = re.split(r'(do\(\)|don\'t\(\))',memory)
    action_block.insert(0,"do()")
    for block in range(len(action_block)):
        if action_block[block] == 'do()':
            print("Should say do()",action_block[block])
            print("Should say some memory",action_block[block+1])
            multipliers, running_total = split_memory_by_mul(action_block[block+1])
            total_multipliers.append(multipliers)
            total_running_total += running_total
        else:
            print("not a do")
    print(total_running_total)
    

def split_memory_by_mul(memory: str):
    print("Memory:",memory)
    # mul_instance = re.split(r'(?=mul\()', memory)
    mul_instance = memory.split('mul(')
    multipliers = []
    running_total = 0
    print("*****")
    for i in mul_instance:
        try:
            mul_func = 'mul(' +i
            print("Partial:",mul_func)
            split_mul = re.split(r'mul\((\d{1,3}),(\d{1,3})\)',mul_func)
            print("Split:",split_mul[1],split_mul[2])
            multipliers.append((split_mul[1],split_mul[2]))
            running_total += int(split_mul[1]) * int(split_mul[2])
            print("M:",multipliers)
        except:
            print('Closing bracket not found')
            print(NameError)
    print("Running total for block:",running_total)
    return multipliers, running_total



memory = read_file('./input.txt')

dodont_output = split_memory_by_dodont(memory)

# multipliers, running_total = split_memory_by_mul(memory)
# print(running_total)
