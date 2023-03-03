# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo._Zoo__animals += 1
#
#     def get_info(self, species):
#         info = ""
#         if species == "mammal":
#             info = f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == "fish":
#             info = f"Fishes in {self.name}: {', '.join(self.mammals)}"
#         elif species == "bird":
#             info = f"Birds in {self.name}: {', '.join(self.mammals)}"
#
#         return f"{info}\nTotal animals: {Zoo._Zoo__animals}"
#
#
# name = input()
# rows = int(input())
#
# zoo = Zoo(name)
#
# for _ in range(rows):
#     species, name = input().split()
#     zoo.add_animal(species, name)
#
# species = input()
# print(zoo.get_info(species))



# ########################################
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         info = ""
#         if species == "mammal":
#             info = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             info = f"Fishes in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "bird":
#             info = f"Birds in {self.name}: {', '.join(self.mammals)}\n"
#
#         info += f"Total animals: {Zoo.__animals}"
#         return info
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
#
# for i in range(count):
#     animal = input().split(" ")
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"

        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for _ in range(number_of_lines):
    info = input().split(' ')
    species = info[0]
    type_of_animal = info[1]
    zoo.add_animal(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))


























