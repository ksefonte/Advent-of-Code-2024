def plog(*input):
    #print(input)
    return

def read_file(file_path: str) -> list:
    output = ""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            output += line
    return output

# 23 33 13 31 21 41 41 31 40 2
# 00...111...2...333.44.5555.6666.777.888899
def process_file(line: str) -> list:
    plog(line)
    if len(line) // 2 != 0:
        line += "0"
    plog("new line:")
    plog(len(line))
    fs_count = 0
    output = []
    for index,i in enumerate(range(0,len(line.strip())-1,2)):
        file = []
        free = []
        # for f in (str(index) * int(line[i])):
        for f in (range(int(line[i]))):
            plog(str(index) * int(line[i]))
            plog("index,i,linei,f",index,i,line[i],f)
            file.append(index)
        output.extend(file)
        for fs in (int(line[i+1]) * '.'):
            plog("i is",line[i+1])
            free.append(fs)
            fs_count += len(fs)
        output.extend(free)
        plog(f'{index}: {line[i],line[i+1]}')
    print(f"initial list: {len(output)} \n{output}")
    buffer = []
    if "." in output:
        while len(buffer) <= fs_count:
            print("Cycling...")
            buffer = []
            print(f"len: {len(buffer)} / {fs_count} ")
            for b in range(len(output)-1):
                print(f"len: {len(buffer)} / {fs_count} ")
                while output[-1] == ".":
                    buffer.extend(output.pop())
                if b < len(output) and output[b] == '.':
                    if output[-1] != ".":
                        output.insert(b,output.pop())
                        output.append(output.pop(b+1))
                        plog(f"Current output: {output}")
                    else:
                        plog("None")
            output.extend(buffer)
            if len(buffer) >= fs_count:
                break
    print("End:",output)
    checksum = 0
    for index,i in enumerate(output):
        if i != ".":
            checksum += (int(i) * index)


    print("Checksum",checksum)



    # for b in range(len(output)-1):
    #     plog(b,"Block:",output[b])
    # plog("=======")
    # for b in range(len(output)-2, -1, -1):
    #     plog(b,"Block:",output[b])
    #     while len(output[b]) > 0:
    #         if len(output[b]) != 0:
    #             temp = output[b].pop()
    #         for a in output:
    #             plog("A:",a)
    #             if "." in a:
    #                     a[a.index(".")] = temp
    #             else:
    #                 plog(f". not found in {a} not found, trying next")
    #             # cont = input("Continue")
    #     plog(f"Finished: {b}")


    plog(output)
    plog(fs_count)

#1 /  3  / 1 / 0 / 6
#0 / ... / 1 / . / 222222

        

process_file(read_file('./input.txt'))