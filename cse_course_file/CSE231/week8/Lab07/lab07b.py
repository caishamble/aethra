import string
from operator import itemgetter


def add_word(word_map, word):
    word = word.lower()

    if word not in word_map:
        word_map[word] = 0

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
    freq_list = sorted(
        (k, v) for k, v in word_map.items() if k.strip()
    )

    freq_list = sorted(freq_list, key=lambda x: (-x[1], x[0]))
    #freq_list = sorted(freq_list, key=itemgetter(1,0),reverse=True)

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