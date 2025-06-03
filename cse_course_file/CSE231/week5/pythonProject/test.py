ALPHABET = "abcdefghijklmnopqrstuvwxyz"
user_input = input("Enter a string: ")
user_input_lower = user_input.lower()
for i in range(len(user_input_lower)):
    if user_input_lower[i] in ALPHABET and user_input_lower[i] != 'a':
        for j in range(len(ALPHABET)):
            if user_input_lower[i] == ALPHABET[j]:
                index = j
                converted_index = 26 - index
                user_input_lower = user_input_lower.replace(user_input_lower[i], ALPHABET[converted_index])
                break
    else:
        continue

print(user_input_lower)