import re

class Letter:
    instances = []
    def __init__(self, x, y, letter):
        self.x: int = x
        self.y: int = y
        self.letter: str = letter
        Letter.instances.append(self)

    def __eq__(self, other):
        if not isinstance(other, Letter):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y) and (self.letter == other.letter)

    def __hash__(self):
        return hash((self.x, self.y, self.letter))

    def __repr__(self):
        return f"Letter {self.letter}, X: {self.x}, Y: {self.y}."
    
    @classmethod
    def find_by_coords(cls, x, y):
        for instance in cls.instances:
            if instance.x == x and instance.y == y:
                    return instance
            
    @classmethod
    def find_by_letter(cls, letter):
        letters = []
        for instance in cls.instances:
            if instance.letter == letter:
                    letters.append(instance)
        return letters
    
    @classmethod
    def list_instances(cls,print_output=False):
        for instance in cls.instances:
            if print_output:
                print(instance)
        return cls.instances
            
    def find_by_delta(self, dx, dy):
       return Letter.find_by_coords(self.x + dx, self.y + dy)
    
    def find_no(self):
        return Letter.find_by_coords(self.x, self.y - 1)
    def find_ne(self):
        return Letter.find_by_coords(self.x + 1, self.y - 1)    
    def find_ea(self):
        return Letter.find_by_coords(self.x + 1, self.y)
    def find_se(self):
        return Letter.find_by_coords(self.x + 1, self.y + 1)
    def find_so(self):
        return Letter.find_by_coords(self.x, self.y + 1)
    def find_sw(self):
        return Letter.find_by_coords(self.x - 1, self.y + 1)
    def find_we(self):
        return Letter.find_by_coords(self.x - 1, self.y)
    def find_nw(self):
        return Letter.find_by_coords(self.x - 1, self.y - 1)

def read_file(file_path: str) -> list:
    word_search = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            word_search.append(line.strip())
    return word_search

def classify_word_search(word_search: list):
    classified_letters = []
    x = 0
    y = 0
    letter = ""
    for i in range(len(word_search)):
        line = (word_search[i])
        y = i
        for j in range(len(line)):
            x = j
            letter = line[j]
            # print("X index:",j)
            # print("Y index:",i)
            # print("Letter:",letter)
            classified_letters.append(Letter(x,y,letter))
    # for classified_letter in classified_letters:
    #     print(classified_letter)
    return classified_letters

def find_mas_xs_from_as(a_instances: list) -> tuple[int, list]:
    ## Find all A's, then search neighbouring coordinates for M and S
    mas_x_sets = []
    total_mas_xs = 0
    methods = ['find_no','find_ne','find_ea','find_se','find_so','find_sw', 'find_we','find_nw']
    roots = [(-1,-1),(1,-1),(1,1),(-1,1),]
    for a in a_instances:
        for root in range(len(roots)):
            root_coords = roots[root]
            root_x,root_y = root_coords
            root_m = a.find_by_delta(*root_coords)
            if root_m and root_m.letter == 'M':
                inverted_root_coords = -root_x,-root_y
                opposite_root_s = a.find_by_delta(*inverted_root_coords)
                if opposite_root_s and opposite_root_s.letter == 'S':
                    reflected_root_coords = -root_x,root_y
                    reflected_root_ms = a.find_by_delta(*reflected_root_coords)
                    if reflected_root_ms and reflected_root_ms.letter == 'M':
                        inverted_reflected_root_coords = root_x,-root_y
                        inverted_opposite_root_s = a.find_by_delta(*inverted_reflected_root_coords)
                        if inverted_opposite_root_s and inverted_opposite_root_s.letter == 'S':
                            total_mas_xs += 1
                            mas_x_sets.append((root_m,a,opposite_root_s,reflected_root_ms,a,inverted_opposite_root_s))
                        else:
                            break
                    elif reflected_root_ms and reflected_root_ms.letter == 'S':
                        inverted_reflected_root_coords = root_x,-root_y
                        inverted_opposite_root_s = a.find_by_delta(*inverted_reflected_root_coords)
                        if inverted_opposite_root_s and inverted_opposite_root_s.letter == 'M':
                            total_mas_xs += 1
                            mas_x_sets.append((root_m,a,opposite_root_s,reflected_root_ms,a,inverted_opposite_root_s))
                        else:
                            break
    return total_mas_xs, mas_x_sets


def find_xmas_instances_from_x(xs: list) -> int:
    ## Every instance of "XMAS" should start at an "X", regardless of orientation.
    total_xmas_sets = []
    total_xmas_instances = 0
    loop_enabled = True
    if loop_enabled:
        s_list = []
        a_list = []
        m_list = []
        methods = ['find_no','find_ne','find_ea','find_se','find_so','find_sw', 'find_we','find_nw']
        for x in xs:
            for method in methods:
                x_neigbhour = getattr(x,method,'None found')()
                if x_neigbhour and x_neigbhour.letter == 'M':
                    m_neighbour = getattr(x_neigbhour,method,'None found')()
                    if m_neighbour and m_neighbour.letter == 'A':
                        a_neighbour = getattr(m_neighbour,method,'None found')()
                        if a_neighbour and a_neighbour.letter == 'S':
                            total_xmas_instances += 1

        # for x in xs:
        #     no_m = x.find_no()
        #     if no_m and no_m.letter == 'M':
        #         no_a = no_m.find_no()
        #         if no_a and no_a.letter == 'A':
        #             no_s = no_a.find_no()
        #             if no_s and no_s.letter == 'S':
        #                 total_xmas_instances +=1
        #                 total_xmas_sets.append((x,no_m,no_a,no_s))
        #     ne = x.find_ne()
        #     ea = x.find_ea()
        #     se = x.find_se()
        #     so = x.find_so()
        #     sw = x.find_sw()
        #     we = x.find_we()
        #     nw = x.find_nw()

        # Spaghetti code - finds non-linear xmases :joy:
        # for x in xs:
        #     print("X is:",x)
        #     x_neighbours = [x.find_no(),x.find_ne(),x.find_ea(),x.find_se(),x.find_so(),x.find_sw(), x.find_we(),x.find_nw()]
        #     for x_neighbour in x_neighbours:
        #         if x_neighbour and x_neighbour.letter == 'M':
        #             print("X neighbour:",x_neighbour)
        #             m_list.append(x_neighbour)
        # for m in m_list:
        #     print("M is",m)
        #     m_neighbours = [m.find_no(),m.find_ne(),m.find_ea(),m.find_se(),m.find_so(),m.find_sw(), m.find_we(),m.find_nw()]
        #     for m_neighbour in m_neighbours:
        #         if m_neighbour and m_neighbour.letter == 'A':
        #             a_list.append(m_neighbour)
        # for a in a_list:
        #     print("A is:",a)
        #     a_neighbours = [a.find_no(),a.find_ne(),a.find_ea(),a.find_se(),a.find_so(),a.find_sw(), a.find_we(),a.find_nw()]
        #     for a_neighbour in a_neighbours:
        #         if a_neighbour and a_neighbour.letter == 'S':
        #             s_list.append(a_neighbour)
        #             total_xmas_instances += 1
        print(len(xs))
        print(len(m_list))
        print(len(a_list))
        print(len(s_list))
    return total_xmas_instances
            
listed_file = read_file('./input.txt')
# print(listed_file)
classified_letters = classify_word_search(listed_file)

# xs = Letter.find_by_letter("X")
# xmases = find_xmas_instances_from_x(xs)
# print("Total xmases:",xmases)

a_instances = Letter.find_by_letter("A")
total_mas_xs, mas_x_sets = find_mas_xs_from_as(a_instances)
# print("MAS x sets:",mas_x_sets)
print("Number of As:",len(a_instances))
print("Total MAS xs:",total_mas_xs)
print("Total unique MAS xs:",len(set(mas_x_sets)))

## today i learned
unique_sets = set(frozenset(mas_xs) for mas_xs in mas_x_sets)
print(len(unique_sets))


        # no = x.find_no().letter if x.find_no() else None
        # ne = x.find_ne().letter if x.find_ne() else None
        # ea = x.find_ea().letter if x.find_ea() else None
        # se = x.find_se().letter if x.find_se() else None
        # so = x.find_so().letter if x.find_so() else None
        # sw = x.find_sw().letter if x.find_sw() else None
        # we = x.find_we().letter if x.find_we() else None
        # nw = x.find_nw().letter if x.find_nw() else None            
        # no = x.find_no()
        # ne = x.find_ne()
        # ea = x.find_ea()
        # se = x.find_se()
        # so = x.find_so()
        # sw = x.find_sw()
        # we = x.find_we()
        # nw = x.find_nw()

        # print(no,ne,ea,se,so,sw,we,nw)