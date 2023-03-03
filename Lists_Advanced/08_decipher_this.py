secret_message = input().split()

for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    #  number is "72"
    first_letter = chr(int(number))  # number is cast to int then to char
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]

    print(f"{''.join(current_word)} ", end="")



