# sort_list() function goes here
def sort_list(a_list):
    a_list.sort()
def main():
    # loop to accept integers until an empty string is entered goes here
    a_list = []
    while True:
        num_str = input()
        if num_str == ' ' or num_str == '':
            break
        else:
            if num_str.isdigit():
                a_list.append(int(num_str))
    ######Do not modify this part######
    print(a_list)
    sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here


if __name__ == "__main__":
    main()