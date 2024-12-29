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
    enable_logs = False
    if enable_logs: print("Raw Updates:",updates)
    total_valid_update_sets = 0
    sum_of_middle_numbers = 0
    ordered_updates = []
    unordered_updates = []
    for update in updates:
        update = update.split(',')
        update_length = len(update)
        middle_update = int(update[int((update_length-1)/2)])
        if enable_logs:
            print("Length is:",update_length,"update is:",update)
            print("middle number is:",middle_update,type(middle_update))
            print("Update:",update)
        valid_updates = 0
        for i in range(update_length):
            if enable_logs:
                print("I is:",i)
                print("Update is:",update)
            if validate_page_position(i,update):
                valid_updates += 1
        if enable_logs:
            print("V,V",valid_updates,len(update))
        if valid_updates == len(update):
            total_valid_update_sets += 1
            sum_of_middle_numbers += middle_update
            ordered_updates.append(update)
        else:
            unordered_updates.append(update)
    return total_valid_update_sets, sum_of_middle_numbers, ordered_updates, unordered_updates

def process_unordered_updates(updates: list):
    enable_logs = True
    print("Raw Updates:",updates)
    reordered_total_valid_update_sets = 0
    reordered_sum_of_middle_numbers = 0
    reordered_ordered_updates = []
    unordered_updates = []
    for update in updates:
        ordered = False
        update_length = len(update)
        # while ordered == False:
        valid_updates = 0
        while valid_updates != update_length:
            valid_updates = 0
            print("Update length",update_length)
            for i in range(update_length):
                if enable_logs:
                    print("I is:",i)
                    print("Update is:",update)
                    print('Select update is:',update[i])
                update_ordered = validate_page_position(i,update)
                if update_ordered:
                    print("Valid order")
                    valid_updates +=1
                elif update_ordered != True:
                    update_to_reorder = update.pop(i)
                    print("RE:",update_to_reorder)
                    update.insert(0,update_to_reorder)
                    valid_updates = 0
        if enable_logs:
            print("V,V",valid_updates,len(update))
        if valid_updates == len(update):
            reordered_total_valid_update_sets += 1
            ordered_updates.append(update)
            middle_update = int(update[int((update_length-1)/2)])
            reordered_sum_of_middle_numbers += middle_update
        else:
            unordered_updates.append(update)
        if enable_logs:
            print("Length is:",update_length,"update is:",update)
            print("Update:",update)
    return reordered_total_valid_update_sets, reordered_sum_of_middle_numbers, reordered_ordered_updates


def validate_page_position(page_index: int, update_set: list):
    # print('Before pop:',update_set)
    # print("Index",page_index)
    working_set = update_set.copy()
    page = working_set.pop(page_index)
    # print("Page:",page)
    # print("Update after pop:",working_set)
    # print("Lenght:",len(working_set))
    rules = Rule.find_by_before(page)
    for i in range(len(working_set)):
        update = working_set[i]
        for rule in rules:
            if update == rule.y and i < page_index:
                return False
    return True

rules = read_file('./input_rules.txt')
updates = read_file('./input_updates.txt')
list_of_rules = classify_rules(rules)
total_valid_update_sets, sum_of_middle_numbers, ordered_updates, unordered_updates = process_updates(updates)
print("Sum of middle numbers is:",sum_of_middle_numbers)
print(len(unordered_updates))
reordered_total_valid_update_sets, reordered_sum_of_middle_numbers, reordered_ordered_updates = process_unordered_updates(unordered_updates)
print("Middle:",reordered_sum_of_middle_numbers)
