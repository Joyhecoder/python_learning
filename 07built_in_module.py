import random

# for i in range(3):
#     print(random.randint(10, 20))

#? get a ramdon element from a list
members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
# print(leader)

#! exercise 
class Dice:
    def __init__(self, name):
        self.name = name
    def roll(self):
        num_list = []
        for i in range(2):
            num = random.random()
            num_list.append(num)
        num_tuple = tuple(num_list)
        return num_tuple

unique_dice = Dice("a dice")
print(unique_dice.name)
print(unique_dice.roll())

#* Mosh's solution:
class Mosh_Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
        # return (first, second)
    