#Slicing

first_string = input()
second_string = input()
last_printed_string = first_string
for char_index in range(len(first_string)):
    left_part = second_string[:char_index + 1] #[0 : char_index + 1 : 1]
    right_part = first_string[char_index + 1:] #[char_index + 1 : len(first_str) : 1]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
