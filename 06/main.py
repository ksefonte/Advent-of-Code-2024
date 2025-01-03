import re
import os
import copy

class Guard:
    def __init__(self, coordinate, direction):
        self.coordinate: Coordinate = coordinate
        self.direction: str = direction
        self.coordinate.contents = direction
        self.movement_dir = direction

    def copy(self):
        return Guard(self.coordinate.copy(), self.direction)
    
    def rotate_guard(self,current_direction):
        logs = False
        directions = ["^",">","V","<"]
        if current_direction in directions:
            self.direction = directions[(directions.index(current_direction) + 1) % len(directions)]
            self.coordinate.contents = self.direction
        if logs: print(f'Was: {current_direction}, is now: {self.direction}')
    
    def move_in_direction(self):
        movement_direction = {
            "^": self.coordinate.move_no,
            ">": self.coordinate.move_ea,
            "V": self.coordinate.move_so,
            "<": self.coordinate.move_we
        }
        if self.direction in movement_direction:
            movement_direction[self.direction]()

    def scout_direction(self):
        scouting_direction = {
            "^": self.coordinate.find_no(),
            ">": self.coordinate.find_ea(),
            "V": self.coordinate.find_so(),
            "<": self.coordinate.find_we()
        }
        if self.direction in scouting_direction:
            return scouting_direction[self.direction]

class Coordinate:
    instances = []
    def __init__(self, x, y, contents):
        self.x: int = x
        self.y: int = y
        self.coords = x,y
        self.contents: str = contents
        if contents =='#':
            self.obstruction = True
        else:
            self.obstruction = False
        Coordinate.instances.append(self)

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y) and (self.contents == other.contents)

    def __hash__(self):
        return hash((self.x, self.y, self.contents))

    def __repr__(self):
        return f"Contents: '{self.contents}'\nX: {self.x}\nY: {self.y}\n"
    
    def copy(self):
        return Coordinate(self.x, self.y, self.contents)
    
    def reset_trails(cls):
        for instance in cls.instances:
            if instance.contents == '|' or '-':
                instance.contents = '.'

    @classmethod
    def find_by_coords(cls, x, y):
        for instance in cls.instances:
            if instance.x == x and instance.y == y:
                    return instance
            
    def check_path(self,target):
        def path_direction(dx,dy):
            print("Self minus target x is ",dx)
            print("Self minus target y is ",dy)
            if dy > 0 and dx == 0:
                print("Scenario 1")
                return dy, -1, "y", "x"
            elif dx > 0 and dy == 0:
                print("Scenario 2")
                return dx, -1, "x", "y"
            elif dy < 0 and dx == 0:
                print("Scenario 3")
                return dy, 1, "y", "x"
            elif dx < 0 and dy == 0:
                print("Scenario 4")
                return dx, 1, "x", "y"
        pathway = []
        obstructions = []
        dx = self.x - target.x
        dy = self.y - target.y
        delta, step, dir, opp = path_direction(dx,dy)
        print(f'self, target,{self.x,self.y,target.x,target.y} | delta, step{delta,step}')
        print(f"dx,dy,{dx,dy}")
        self_opp = getattr(self,opp)
        target_opp = getattr(target,opp)
        self_dir = getattr(self,dir)
        target_dir = getattr(target,dir)
        print(f"Self, target dir {dir, self_dir, target_dir} step {step}")
        if getattr(self,opp) == getattr(target,opp):
        # if self.x == target.x or self.y == target.y:
            for index,i in enumerate(range(self_dir,target_dir,step)):
                print("I is:",i)
                dir_val = getattr(self,dir)
                opp_val = getattr(self,opp)
                print(f"Dir,opp {dir, dir_val+(step*index), opp, opp_val}")
                if dir == 'x':
                    coord = Coordinate.find_by_coords(dir_val+(step*index),opp_val)
                    if coord.contents != "#":
                        print("C:",coord)
                        pathway.append(coord)
                        # print("P",pathway)
                    else:
                        print("Obstruction found")
                        obstructions.append(coord)
                elif dir == 'y':
                    coord = Coordinate.find_by_coords(opp_val,dir_val+(step*index))
                    if coord.contents != "#":
                        print("C:",coord)
                        pathway.append(coord)
                        # print("P:",pathway)
                    else:
                        print("Obstruction found")
                        obstructions.append(coord)
        print("Delta:",delta)
        print("Pathway length:",len(pathway))
        print("Obstruction length:",len(obstructions))
        if len(pathway) > 0 and len(obstructions) == 0:
            print("Clear path")
            return True
        
        else:
            print("Obstructed path")
            return False

    def move_by_coords(self,x,y,trail=False):
        trail=True
        target_guardinate = Coordinate.find_by_coords(x,y)
        dx = target_guardinate.x - x
        dy = target_guardinate.y - y
        if target_guardinate:
            target_guardinate.x, self.x = self.x, target_guardinate.x
            target_guardinate.y, self.y = self.y, target_guardinate.y
            if trail and dy == 0:
                target_guardinate.contents = '-'
            elif trail and dx == 0:
                target_guardinate.contents = '|'
        else:
            input("Continue")
            print("Target coordinate not found")
            
    @classmethod
    def find_by_contents(cls, contents):
        contents_list = []
        for instance in cls.instances:
            if instance.contents == contents:
                    contents_list.append(instance)
        if contents == '^':
            if len(contents_list) == 1:
                return contents_list[0]
            else:
                print('Error, more than one Guard found')
                return None
        else:
            return contents_list
    
    @classmethod
    def list_instances(cls,print_output=False):
        if print_output: print("Printing instances")
        for instance in cls.instances:
            if print_output:
                print(instance)
        return cls.instances
    
    def find_nesw(self):
        return self.find_no(), self.find_ea(), self.find_so(), self.findwe()
    
    def find_by_delta(self, dx, dy):
       return Coordinate.find_by_coords(self.x + dx, self.y + dy)
    def find_no(self):
        return Coordinate.find_by_coords(self.x, self.y - 1)
    def find_ne(self):
        return Coordinate.find_by_coords(self.x + 1, self.y - 1)    
    def find_ea(self):
        return Coordinate.find_by_coords(self.x + 1, self.y)
    def find_se(self):
        return Coordinate.find_by_coords(self.x + 1, self.y + 1)
    def find_so(self):
        return Coordinate.find_by_coords(self.x, self.y + 1)
    def find_sw(self):
        return Coordinate.find_by_coords(self.x - 1, self.y + 1)
    def find_we(self):
        return Coordinate.find_by_coords(self.x - 1, self.y)
    def find_nw(self):
        return Coordinate.find_by_coords(self.x - 1, self.y - 1)
    
    def move_no(self):
        return self.move_by_coords(self.x, self.y - 1)
    def move_ea(self):
        return self.move_by_coords(self.x + 1, self.y)
    def move_so(self):
        return self.move_by_coords(self.x, self.y + 1)
    def move_we(self):
        return self.move_by_coords(self.x - 1, self.y)

def read_file(file_path: str) -> list:
    word_search = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            word_search.append(line.strip())
    return word_search

def classify_prison_coordinates(prison_grid: list):
    classified_coordinates = []
    for i in range(len(prison_grid)):
        line = (prison_grid[i])
        for j in range(len(line)):
            contents = line[j]
            classified_coordinates.append(Coordinate(j,i,contents))
    return classified_coordinates

def reset_grid(classified_coordinates: list) -> list:
    Coordinate.instances.clear()
    return [Coordinate(coord.x, coord.y, coord.contents) for coord in classified_coordinates]

def map_path(classified_coordinates: list) -> None:
    logs = False
    if logs: print("Mapping path")
    guard_coord = Coordinate.find_by_contents('^')
    tiles_walked = [guard_coord.coords]
    if logs: print('Guard coord:',guard_coord.x, guard_coord.y)
    guard = Guard(guard_coord,'^').copy()
    current_direction = guard.direction
    scout_tile = guard.scout_direction()
    while scout_tile:
        root_length = 0
        if logs:
            print("Tiles all walked:",tiles_walked)
            print("distance walked:",len(tiles_walked))
            print("Scout tile:",scout_tile)
        if scout_tile and not scout_tile.obstruction:
            tiles_walked.append(guard.coordinate.copy().coords)
            if logs: print('Guard:',guard.coordinate)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
        elif scout_tile and scout_tile.obstruction:
            if logs: print("Obstruction found, turning")
            tiles_walked.append(guard.coordinate.copy().coords)
            guard.rotate_guard(current_direction)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
    # for coordinate in classified_coordinates:
    #     guard = coordinate.find_by_contents('X')
    return tiles_walked

def map_and_obstaclate(classified_coordinates: list) -> None:
    obstructions = []
    newlogs = True
    logs = False
    if logs: print("Mapping path")
    obstacles_positions = []
    guard_coord = Coordinate.find_by_contents('^')
    tiles_walked = [guard_coord]
    if logs: print('Guard coord:',guard_coord.x, guard_coord.y)
    guard = Guard(guard_coord,'^')
    save_state = guard.copy()
    current_direction = guard.direction
    scout_tile = guard.scout_direction()
    while scout_tile:
        root_length = 0
        if logs:
            print("Tiles all walked:",tiles_walked)
            print("distance walked:",len(tiles_walked))
            print("Scout tile:",scout_tile)
        if scout_tile and not scout_tile.obstruction:
            tiles_walked.append(guard.coordinate.copy().coords)
            if logs: print('Guard:',guard.coordinate)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
        elif scout_tile and scout_tile.obstruction:
            if newlogs: print("Obstruction found, turning")
            obstructions.append((scout_tile,guard.coordinate.copy()))
            tiles_walked.append(guard.coordinate.copy().coords)
            guard.rotate_guard(current_direction)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
    # for coordinate in classified_coordinates:
    #     guard = coordinate.find_by_contents('X')
    return tiles_walked, obstructions, classified_coordinates

def map_and_declare_loop(classified_coordinates: list, ipass: int) -> None:
    obstructions = []
    newlogs = False
    logs = False
    repeat_tiles = 0
    if logs: print("Mapping path")
    for x in classified_coordinates:
        if x.contents == '^':
            print('Guard found',x)
            guard_coord = x
        else:
            print("Guard not found",ipass)
    tiles_walked = []
    initial_guard = Guard(guard_coord,'^').copy()
    guard = initial_guard.copy()
    print('Guard coord:',guard_coord.x, guard_coord.y, id(guard_coord), id(guard))
    current_direction = guard.direction
    scout_tile = guard.scout_direction()
    while scout_tile and repeat_tiles < 1:
        if logs:
            print("Tiles all walked:",tiles_walked)
            print("distance walked:",len(tiles_walked))
            print("Scout tile:",scout_tile)
        if scout_tile and not scout_tile.obstruction:
            the_tuple = ((guard.coordinate.copy().coords, guard.direction))
            print("the tuple:",the_tuple)
            if the_tuple in tiles_walked:
                repeat_tiles += 1
                print("Found repeat")
            else:
                print(f"{ipass} Repeat not found yet.")
            tiles_walked.append((guard.coordinate.copy().coords, guard.direction))
            if logs: print('Guard:',guard.coordinate)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
        elif scout_tile and scout_tile.obstruction:
            the_tuple = ((guard.coordinate.copy().coords, guard.direction))
            print("the tuple:",the_tuple)
            if the_tuple in tiles_walked:
                repeat_tiles += 1
                print(f"{ipass} Found repeat")
            else:
                print("Repeat not found yet.")
            if newlogs: print("Obstruction found, turning")
            obstructions.append((scout_tile,guard.coordinate.copy()))
            tiles_walked.append((guard.coordinate.copy().coords,guard.direction))
            guard.rotate_guard(current_direction)
            guard.move_in_direction()
            scout_tile = guard.scout_direction()
            current_direction = guard.direction
    # for coordinate in classified_coordinates:
    #     guard = coordinate.find_by_contents('X')
    return set(tiles_walked)

def brute_force_grid_legacy(classified_coordinates: list, walked_tiles: list):
    print("classified_coordinates")
    print(classified_coordinates)
    print("=================================")
    tiles_walked_list = []
    initial_grid = reset_grid(classified_coordinates)
    for i in range(len(initial_grid)):
    # for i in range(len(classified_coordinates)):
        working_coordinates = reset_grid(initial_grid)
        print("Pass:",i+1)
        if working_coordinates[i].contents not in ('^','#'):
            print("Obstaclating...")
            print(working_coordinates[i])
            working_coordinates[i].contents = '#'
            working_coordinates[i].obstruction = True
            tiles_walked = map_and_declare_loop(working_coordinates, i)
            tiles_walked_list.append(len(tiles_walked))
        elif working_coordinates[i].contents == '^':
            print("Error, found guard")
    print(len(tiles_walked_list))

def brute_force_grid(classified_coordinates: list, walked_tiles: list):
    print("classified_coordinates")
    unique_tiles_walked = list(set(walked_tiles))
    print(len(
        unique_tiles_walked
    ))
    print(classified_coordinates)
    print("walked_tiles",len(walked_tiles))
    print(walked_tiles)
    print("=================================")
    tiles_walked_list = []
    initial_grid = reset_grid(classified_coordinates)
    for i in range(200):
    # for i in range(len(classified_coordinates)):
        working_coordinates = reset_grid(initial_grid)
        print("Pre:",unique_tiles_walked[i])
        obstacle_to_place = Coordinate.find_by_coords(*unique_tiles_walked[i])
        print("Pass:",i+1)
        if obstacle_to_place.contents not in ('^','#'):
            print("Obstaclating...")
            print(obstacle_to_place)
            obstacle_to_place.contents = '#'
            obstacle_to_place.obstruction = True
            tiles_walked = map_and_declare_loop(working_coordinates, i)
            tiles_walked_list.append(len(tiles_walked))
        elif working_coordinates[i].contents == '^':
            print("Error, found guard")
    print(len(tiles_walked_list))
        

def place_obstructions(obstructions: tuple) -> int:
    """Finds instances of a square loop. Not the correct solution >.>"""
    print("Obs length:",len(obstructions))
    oset = []
    for i in range(len(obstructions)-2):
        logging = True
        print(f'Pass number {i+1} set {len(oset)}')
        # print(obstructions[i])
        print("______________")
        obstruction1,guard1 = obstructions[i]
        print("o,g",obstruction1,guard1)
        dx1 = guard1.x - obstruction1.x
        dy1 = guard1.y - obstruction1.y

        obstruction2,guard2 = obstructions[i+1]
        dx2 = guard2.x - obstruction2.x
        dy2 = guard2.y - obstruction2.y

        obstruction3,guard3 = obstructions[i+2]
        dx3 = guard3.x - obstruction3.x
        dy3 = guard3.y - obstruction3.y

        g4x = guard1.x ^ guard2.x ^ guard3.x
        g4y = guard1.y ^ guard2.y ^ guard3.y

        d4x = dx1-dx2+dx3
        d4y = dy1-dy2+dy3

        if logging:
            print(f"1.){guard1.x}, {guard1.y} ({dx1,dy1}) ")
            print(f"2.){guard2.x}, {guard2.y} ({dx2,dy2}) ")
            print(f"3.){guard3.x}, {guard3.y} ({dx3,dy3}) ")
            print(f'G.){g4x,g4y}')
            print(f'O.){d4x,d4y} (offset eg 1/1,0/1,-1/0,0/-1)')

        if (guard1.x + guard3.x - guard2.x - g4x == 0) and (guard1.y + guard3.y - guard2.y - g4y == 0):
            print("Square, checking validity...")
            target_guard = Coordinate.find_by_coords(g4x,g4y)
            target_obs = Coordinate.find_by_coords(g4x-d4x,g4y-d4y)
            print(f'Target coordinate: \n{target_guard}')
            if target_guard and target_obs and target_obs.contents != '#':
                if guard3.check_path(target_guard):
                    oset.append(target_guard)
                else:
                    print("Path not clear")
                print("Target:",target_guard.x,target_guard.y)
        else: print("Not square")
        print("/////////////////////////////////////////////////////////////////////////")
        yes = input("hello")
    print("Fulll set")
    print(len(oset))
    print(len(set(oset)))
    return set(oset)

listed_file = read_file('./input.txt')
classified_coordinates = classify_prison_coordinates(listed_file)
initial_coordinates = reset_grid(classified_coordinates)
tiles_walked = map_path(classified_coordinates)
print(tiles_walked)
print(len(set(frozenset(tiles_walked))))

bf_coordinates = reset_grid(initial_coordinates)
brute_force_grid(bf_coordinates,tiles_walked)

# tiles_walked, obstructions = map_and_obstaclate(classified_coordinates)
# print("Total walked:",len(set(tiles_walked)))
# oset = place_obstructions(obstructions)
# print("Set",len(oset))

    # print('Obstruction:\n',obstruction)
    # print("----")
    # print('Guard:\n',guard)
    # print("==========")

