import string
from operator import itemgetter


def add_word(word_map, word):
    # YOUR COMMENT
    if word not in word_map:
        word_map[word] = 0

    # YOUR COMMENT
    word_map[word] += 1


def build_map(in_file, word_map):
    for line in in_file:

        # YOUR COMMENT
        word_list = line.split()

        for word in word_list:
            # YOUR COMMENT
            word = word.strip().strip(string.punctuation)
            add_word(word_map, word)


def display_map(word_map):
    # YOUR COMMENT
    freq_list = sorted(word_map.items(), key=itemgetter(1))

    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file():
    file_exists = False

    while not file_exists:
        try:
            file_name = input("Enter file name: ")
            fp = open(file_name, "r")
            return fp

        except FileNotFoundError:
            print("\n*** unable to open file ***\n")


def main():
    word_map = {}
    in_file = open_file()
    print()
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()


main()