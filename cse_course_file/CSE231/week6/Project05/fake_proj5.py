###################################################################
# Project 5 - Yu-Gi-Oh! Card Data Analysis
# Mind for main code
# prompt the user for the name of the file and option
# use a while true to keep working
# if option is 1, display the number of cards and the first 50 cards
# if option is 2, prompt the user for a query and category to search
# if option is 3, prompt the user for the name of the file and display the decklist
# if option is 4, exit the program
# if option is invalid, display an error message
###################################################################
import csv

"\nFile not Found. Please try again!"

"{'Name'}{'Type'}{'Race'}{'Archetype'}{'TCGPlayer'}"
"{}{}{}{}{}"
"\n{'Totals'}{''}{''}{''}{}"

"\nThe price of the least expensive card(s) is {}"
"\nThe price of the most expensive card(s) is {}"
"\nThe price of the median card(s) is {}"
"\t{}" #display the cards after the search

"\nInvalid option. Please try again!"
"\nEnter cards file name: "
"\nThere are {} cards in the dataset."
"\nEnter query: "
"\nEnter category to search: "
"\nIncorrect category was selected!"
"\nSearch results"
"\nThere are {} cards with '{}' in the '{}' category."
"\nThere are no cards with '{}' in the '{}' category."
"\nEnter decklist filename: "
"\nThanks for your support in Yu-Gi-Oh! TCG"

MENU = "\nYu-Gi-Oh! Card Data Analysis" \
           "\n1) Check All Cards" \
           "\n2) Search Cards" \
           "\n3) View Decklist" \
           "\n4) Exit" \
           "\nEnter option: "
CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]
def open_file(prompt_str):
    """
    Open file function
    :param prompt_str: prompt string
    :return: file pointer
    """
    while True:
        try:
            # open the file
            fp = open(input(prompt_str), "r", encoding="utf-8")
            return fp
        except FileNotFoundError:
            print("\nFile not Found. Please try again!")
def read_card_data(fp):
    """
    Read card data function
    input the file_pointer and return the card data list (sorted by item 7 and item 2 (name)
    :param fp: file pointer
    :return: card data list
    """
    # read the file
    reader = csv.reader(fp)
    next(reader, None)
    # create a list to store the data
    initial_card_data = []
    for row in reader:
        initial_card_data.append((row[0], row[1][:45], row[2], row[3], row[4], row[5], float(row[6])))
    card_data = sorted(initial_card_data, key=lambda x: (x[6], x[1]))
    return card_data
def search_cards(card_data, query, category_index):
    """
    Search cards function
    input the card data list, query string, and category index and return the final list whose
    category index contains the query string
    :param card_data: card data list
    :param query: query string
    :param category_index: category index
    :return: final list
    """
    final_list = [card for card in card_data if query in card[category_index]]
    return final_list
def read_decklist(fp, card_data):
    """
    Read decklist function
    input the file_pointer and card data list and return the sorted one list whose
    category index contains the query string
    :param fp: file pointer
    :param card_data: card data list
    :return: sorted one list
    """
    one_list = [card_data[q] for row in fp for q in range(len(card_data)) if row.strip() == card_data[q][0]]
    sorted_one_list = sorted(one_list, key=lambda x: (x[6], x[1]))
    return sorted_one_list
def compute_stats(card_data):
    """
    Compute stats function
    input the card data list and return the min, max, and median list and price
    :param card_data: card data list
    :return: min, max, and median list and price
    """
    prices = [float(card[6]) for card in card_data]
    min_price = min(prices)
    max_price = max(prices)
    result_card_data = sorted(card_data, key=lambda x: x[6])
    # calculate the median price
    if len(result_card_data) % 2 == 0:
        med_price = max(float(result_card_data[len(result_card_data) // 2][6]),float(result_card_data[(len(result_card_data) // 2) - 1][6]))
    else:
        med_price = float(result_card_data[len(result_card_data) // 2][6])
    # create the min, max, and median list
    min_list = [card for card in card_data if float(card[6]) == min_price]
    max_list = [card for card in card_data if float(card[6]) == max_price]
    med_list = [card for card in card_data if float(card[6]) == med_price]
    # sort the min, max, and median list
    result_min_list = sorted(min_list, key=lambda x: x[1])
    result_max_list = sorted(max_list, key=lambda x: x[1])
    result_med_list = sorted(med_list, key=lambda x: x[1])
    return result_min_list, min_price, result_max_list, max_price, result_med_list, med_price
def display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price):
    """
    Display stats function
    input the min, max, and median list and price and display the result
    :param min_cards: min list
    :param min_price: min price
    :param max_cards: max list
    :param max_price: max price
    :param med_cards: median list
    :param med_price: median price
    :return: None
    """
    print(f"\nThe price of the least expensive card(s) is {min_price:,.2f}")
    for row in min_cards:
        print(f"\t{row[1]}")
    print(f"\nThe price of the most expensive card(s) is {max_price:,.2f}")
    for row in max_cards:
        print(f"\t{row[1]}")
    print(f"\nThe price of the median card(s) is {med_price:,.2f}")
    for row in med_cards:
        print(f"\t{row[1]}")

def display_data(card_data):
    """
    Display data function
    input the card data list and display the first 50 cards and total price
    :param card_data: card data list
    :return: None
    """
    totals = 0
    print(f"{'Name':<50}{'Type':<30}{'Race':<20}{'Archetype':<40}{'TCGPlayer':<12}")
    counter = 0
    for i in range(len(card_data)):
        if counter == 50:
            break
        else:
            print(f"{card_data[i][1]:<50}{card_data[i][2]:<30}{card_data[i][4]:<20}{card_data[i][5]:<40}{card_data[i][6]:>12,.2f}")
            totals += float(card_data[i][6])
            counter += 1
    print(f"\n{'Totals':<50}{'':<30}{'':<20}{'':<40}{totals:>12,.2f}")
def main():
    """
    Main function
    """
    # open the file and read the data
    fp = open_file("\nEnter cards file name: ")
    card_data = read_card_data(fp)
    # prompt the user for the option
    option = input(MENU)
    while True:
        if option == '1':
            print(f"\nThere are {len(card_data)} cards in the dataset.")
            display_data(card_data)
            # compute the stats
            card_min, prize_min, card_max, prize_max, card_med, prize_med = compute_stats(card_data)
            # display the stats
            display_stats(card_min, prize_min, card_max, prize_max, card_med, prize_med)
            option = input(MENU)
        elif option == '2':
            query = input("\nEnter query: ")
            # use the while loop to keep working
            while True:
                input_category = (input("\nEnter category to search: ")).lower()
                if input_category in CATEGORIES:
                    # get the category index
                    category_index = CATEGORIES.index(input_category)
                    # search the cards
                    final_list = search_cards(card_data, query, category_index)
                    # display the result
                    if len(final_list) == 0: # if there are no cards
                        print(f"\nSearch results")
                        print(f"\nThere are no cards with '{query}' in the '{input_category}' category.")
                    else:
                        print(f"\nSearch results")
                        print(f"\nThere are {len(final_list)} cards with '{query}' in the '{input_category}' category.")
                        display_data(final_list)
                        card_min, prize_min, card_max, prize_max, card_med, prize_med = compute_stats(final_list)
                        display_stats(card_min, prize_min, card_max, prize_max, card_med, prize_med)
                    break
                else:
                    print("\nIncorrect category was selected!")
            option = input(MENU)
        elif option == '3':
            # open the file and read the decklist
            filename = input("\nEnter decklist filename: ")
            ydk = open(filename, "r", encoding="utf-8")
            print(f"\nSearch results")
            # read the decklist
            decklist = read_decklist(ydk, card_data)
            display_data(decklist)
            # compute the stats
            card_min, prize_min, card_max, prize_max, card_med, prize_med = compute_stats(decklist)
            display_stats(card_min, prize_min, card_max, prize_max, card_med, prize_med)
            option = input(MENU)
        elif option == '4':
            print("\nThanks for your support in Yu-Gi-Oh! TCG")
            break
        else:
            print("\nInvalid option. Please try again!")
            option = input(MENU)
if __name__ == "__main__":
    main()
