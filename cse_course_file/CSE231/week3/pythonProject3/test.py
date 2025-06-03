VOWELS = "aeiou"

while True:
    user_input = input().strip()
    if user_input.lower() == "quit":
        break

    word = user_input.lower()
    if word[0] in VOWELS:
        pig_latin_word = word + "way"
    else:
        for i, ch in enumerate(word):
            if ch in VOWELS:
                pig_latin_word = word[i:] + word[:i] + "ay"
                break
        else:
            pig_latin_word = word + "ay"

    print(pig_latin_word)
