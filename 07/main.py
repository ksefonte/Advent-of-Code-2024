from typing import List
import itertools as itt

def read_file(file_path: str) -> list:
    file_out = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            an, eq = line.split(':')
            eq = eq.strip().split(' ')
            file_out.append((an,eq))
    return file_out

def operate(
        i: int,
        j: int,
        operator: str
        ) -> None:
    if operator == '+':
        print('Plussing')
        print(i+j)
        return i + j
    elif operator == '*':
        print('multipling')
        print(i*j)
        return i * j
    else:
        print("Error")
        return None
    
### product func for reference
### https://stackoverflow.com/questions/61049172/explanation-of-the-python-itertools-product-implementation
def product_nocomp(*args):
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        _temp = []
        for x in result:
            for y in pool:
                _temp.append(x + [y])
        result = _temp
    for prod in result:
        yield tuple(prod)
    
def process_an_eq(an: int, eq: List[int]):
    output = None
    operators = ['+','*']
    iterations = itt.product(operators, repeat=len(eq)-1)
    for iteration in iterations:
        base = int(eq[0])
        for num in range(len(iteration)):
            print("B:",base)
            print(f"Base, eqnum, iter {base, int(eq[num+1]), iteration[0]}")
            base = operate(int(base),int(eq[num+1]),iteration[num])
            print("A:",base)
        if base == int(an.strip()):
            return base

file_out = read_file('./input.txt')
print(file_out)

list_of_bases = []
for an,eq in file_out:
    print(f"an, eq: {an,eq}")
    list_of_bases.append(process_an_eq(an,eq))

print("Before filter")
print(list_of_bases)
list_of_bases  = [base for base in list_of_bases if base != None]

print("List of bases:")
print(list_of_bases)
print(sum(list_of_bases))