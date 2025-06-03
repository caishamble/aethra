import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']


def read_file(fp):
    data = []
    reader = csv.reader(fp)
    next(reader,None)
    next(reader,None)
    next(reader,None)
    next(reader,None)

    for row in reader:
        data.append(row)
        break

    next(reader,None)
    for row in reader:
        data.append(row)
    return data

def get_totals(L):
    # Initialize variables to store the sum and the unauthorized immigrant population for the US
    total_sum = 0
    us_population = 0
    for row in L:
        if row[0] == "U.S.":
            us_population = int(row[1].replace("<", "").replace(",", ""))
        else:
            population = int(row[1].replace("<", "").replace(",", ""))
            total_sum += population
    return us_population, total_sum


def get_industry_counts(L):
    counters = [[i, 0] for i in INDUSTRIES]
    for item in L[1:]:
        industry = item[9]
        for i in counters:
            if i[0] == industry:
                i[1] += 1

    counters = sorted(counters, key=itemgetter(1), reverse=True)
    return counters

def get_largest_states(L):
    largest_states = []
    us_value = None
    for row in L:
        if row[0] == "U.S.":
            us_value = float(row[2].replace("%", ""))
            break
    if us_value is None:
        return largest_states
    for row in L:
        if row[2] != '' and float(row[2].replace("%","")) > us_value:
            largest_states.append(row[0])
    largest_states = sorted (largest_states, key = itemgetter(1))
    return largest_states

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
