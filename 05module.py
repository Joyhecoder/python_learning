#functions are stored in converters.py
#? import a whole module
import converters
# print(converters.kg_to_lbs(70))

#?import a certain function in a module
from converters import lbs_to_kg
# print(lbs_to_kg(100))

#! exercise - function is located in utils.py
from utils import find_max
numbers = [10, 3, 6, 2]
# print(find_max(numbers))