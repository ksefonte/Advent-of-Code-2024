def read_file(file_path: str) -> tuple:
    list_1 = []
    list_2 = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.split()
            if line[0]:
                list_1.append(line[0])
                print(line[0])
            try:
                list_2.append(line[1])
                print(line[1])
            except:
                print("Error: Missing second value of value-pair")
        if (len(list_1) == len(list_2)) & (len(list_1) != 0):
            print("Success")
            print("Length of both lists is: ", len(list_1))
        else:
            print("Error: Lists not of equal length")
    return list_1,list_2

def count_difference(list_pair: tuple) -> int:
    output_list = []
    total_delta = 0
    list_1 = list_pair[0]
    list_1.sort()
    list_2 = list_pair[1]
    list_2.sort()
    delta = [abs(int(i) - int(j)) for i,j in zip(list_1,list_2)]
    print("Delta is: ",delta)
    return sum(delta)
    # for i,j in list_1,list_2:
    #     delta = abs(int(i) - int(j))
    #     total_delta =+ delta
    #     print("Delta is: ", delta)
    #     print("Total Delta is: ", total_delta)
    #     output_list.append(delta)

def calculate_similarity(list_pair: tuple) -> int:
    output_list = []
    total_similarity = 0
    list_1 = list_pair[0]
    list_1.sort()
    list_2 = list_pair[1]
    list_2.sort()
    for i in list_1:
        individual_similarity = 0
        for j in list_2:
            if i == j:
                individual_similarity += int(j)
        if individual_similarity != 0:
            print("Similarity score for: ", i , " is:", individual_similarity)
        total_similarity += individual_similarity
    return total_similarity

list_pair = read_file('./input.txt')
print("---")
print("difference:")
print(count_difference(list_pair))
print("---")
print("similarity:")
print(calculate_similarity(list_pair))
