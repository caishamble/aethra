def list_to_tuple(a_list):
    flag = True
    a_tuple = tuple()
    for i in range(len(a_list)):
        if a_list[i].isdigit():
            a_list[i] = int(a_list[i])
            a_tuple += (a_list[i],)
        else:
            flag = False
    if flag:
        print(a_tuple)
    else:
        print("Error. Please enter only integers.")
def main():
    a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
    list_to_tuple(a_list)


if __name__ == "__main__":
    main()
