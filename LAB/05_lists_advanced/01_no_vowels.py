# text = input()
# vowels = 'aouei'
# print("".join([x for x in text if x.lower() not in vowels]))
#

customers = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 44000)]

whales = []
for customer, income in customers:
    if income > 1000000:
        whales.append(customer)
print(whales)

# list comprehension
whales = [x for x, y in customers if y > 1000000]
print(whales)
