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
    elif operator == "||":
        print("Cocatenifying")
        print(i+j)
        string = str(i)+str(j)
        return int(string)
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
    
def process_an_eq(an: int, eq: List[int], operators=['+','*']):
    output = None
    operators = ['+','*','||']
    iterations = itt.product(operators, repeat=len(eq)-1)
    for iteration in iterations:
        base = int(eq[0])
        for num in range(len(iteration)):
            print(an, "B:",base)
            print(f"{an} Base, eqnum, iter {base, int(eq[num+1]), iteration[0]}")
            base = operate(int(base),int(eq[num+1]),iteration[num])
            print(an, "A:",base)
        if base == int(an.strip()):
            return base, (None,None)
    return 0, (an, eq)
    

file_out = read_file('./input.txt')
print(file_out)

list_of_bases = []
for an,eq in file_out:
    print(f"an, eq: {an,eq}")
    list_of_bases.append(process_an_eq(an,eq))

print("Fails:")
failed_calibrations = [(an,eq) for base, (an,eq) in list_of_bases if an != None and eq != None]
print(failed_calibrations)
list_of_bases  = [base for base, (an,eq) in list_of_bases if base != None]
print(list_of_bases)

for an,eq in failed_calibrations:
    print(f"an, eq: {an,eq}")
    base, (an,eq) = process_an_eq(an,eq,operators=['+','*','||'])
    list_of_bases.append(base)
list_of_bases  = [base for base in list_of_bases if base != None]

print("List of bases:")
print(list_of_bases)
print(sum(list_of_bases))