from pathlib import Path

#Absolute path - start from the root of the directory
#Relative path - from current directory 

#? check if a dir exists
# path = Path("ecommerce")
# print(path.exists())

#? create a new dir
# path = Path("emails")
# print(path.mkdir())

#? remove a dir
# print(path.rmdir())

#? find all the files in a dir
path = Path()
print(path.glob('*'))  #=> this returns a <generator object> which can be looped through
for file in path.glob('*.py'):
    print(file)