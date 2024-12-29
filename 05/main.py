class Rule:
    instances = []
    def __init__(self, x, y):
        ### x is 'before', y is 'after'
        self.x: int = x
        self.y: int = y
        Rule.instances.append(self)

    def __eq__(self, other):
        if not isinstance(other, Rule):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Before: {self.x}, After: {self.y}"
    
    @classmethod
    def find_by_before(cls, x):
        return [instance for instance in cls.instances if instance.x == x]

def read_file(file_path: str) -> list:
    file_output = []
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        for line in file_lines:
            file_output.append(line.strip())
    return file_output

def classify_rules(rules: list):
    list_of_rules = []
    for unprocessed_rule in rules:
        before,after = unprocessed_rule.split('|')
        list_of_rules.append(Rule(before,after))
    print('Rules processed')
    return list_of_rules

def process_updates(updates: list):
    print("Raw Updates:",updates)
    total_valid_update_sets = 0
    sum_of_middle_numbers = 0
    list_of_updates = []
    for update in updates:
        update = update.split(',')
        update_length = len(update)
        print("Length is:",update_length,"update is:",update)
        middle_update = int(update[int((update_length-1)/2)])
        print("middle number is:",middle_update,type(middle_update))
        print("Update:",update)
        valid_updates = 0
        for i in range(update_length):
            print(len(update))
            # befores = Rule.find_by_before(update[i])
            print("I is:",i)
            print("Update is:",update)
            if validate_page_position(i,update):
                valid_updates += 1
        print("V,V",valid_updates,len(update))
        if valid_updates == len(update):
            total_valid_update_sets += 1
            sum_of_middle_numbers += middle_update

    return total_valid_update_sets, sum_of_middle_numbers

def validate_page_position(page_index: int, update_set: list):
    print('Before pop:',update_set)
    print("Index",page_index)
    working_set = update_set.copy()
    page = working_set.pop(page_index)
    print("Page:",page)
    print("Update after pop:",working_set)
    print("Lenght:",len(working_set))
    rules = Rule.find_by_before(page)
    for i in range(len(working_set)):
        print(i)
        update = working_set[i]
        for rule in rules:
            if update == rule.y and i < page_index:
                return False
    return True


rules = read_file('./input_rules.txt')
updates = read_file('./input_updates.txt')
list_of_rules = classify_rules(rules)
total_valid_update_sets, sum_of_middle_numbers = process_updates(updates)
print("Sum of middle numbers is:",sum_of_middle_numbers)