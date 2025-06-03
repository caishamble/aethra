import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']


def read_file(fp):
    '''Docstring'''
    return None  # temoprary return value so main runs


def get_totals(L):
    '''Docstring'''
    return None, None  # temoprary return value so main runs


def get_industry_counts(L):
    '''Docstring'''
    return None  # temoprary return value so main runs


def get_largest_states(L):
    '''Docstring'''
    return None  # temoprary return value so main runs


def main():
    fp = open("immigration.csv")
    L = read_file(fp)

    us_pop, total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)

    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n', ' ')
            print(state)

    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry", "count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0], tup[1]))


if __name__ == "__main__":
    main()
