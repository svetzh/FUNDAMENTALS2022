def custom_split(text, sep):  # parameters --> text, sep
    result = text.split(sep)
    return result


print(custom_split("Hello;there", ";"))  # arguments --> "Hello, there" "," true data
print(custom_split("How are you", " "))
print(custom_split("blue,green,red", ","))