#######################################################################################################################################
#  CSE 231 Project #3
#  Algorithm
#  Front work
#  1. Print the basic background info
#  2. Keep down all the constants and strings that will be used in the program
#  Main part
#  1. Use while loop to keep the program running (while True)
#  2. Use if statement to judge the input of square_footage, max_monthly_payment, apr, and reform them
#  3. Use if statement to judge the location_user and calculate the home_cost, P, monthly_tax, monthly_mortgage_payment, monthly_payment
#     i)   case1: only square_footage is known, output the result according to the question
#     ii)  case2: both square_footage and max_monthly_payment are known, output the result according to the question
#     iii) case3: only max_monthly_payment is known, output the result according to the question
#     iv)  case4: neither square_footage nor max_monthly_payment is known, output the result according to the question
#     specially, in each part, if the user input a unknown location, use the average national price per square foot and tax rate
#     Also in each part, if the user want to print the amortization table, use the for loop to print the table
#######################################################################################################################################



# all the constants that will be used in the program
N = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

# all the strings that will be used in the program
WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? '''
SQUARE_FOOTAGE_TEXT = '''\nWhat is the maximum square footage you are considering? '''
MAX_MONTHLY_PAYMENT_TEXT = '''\nWhat is the maximum monthly payment you can afford? '''
DOWN_PAYMENT_TEXT = '''\nHow much money can you put down as a down payment? '''
APR_TEXT = '''\nWhat is the current annual percentage rate? '''

AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''
LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.'''

KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''


# print the basic background info
print(WELCOME_TEXT)
print(MAIN_PROMPT)


# use while loop to keep the program running
while True:

    # all the variables that will be used in the program
    location_user = input(LOCATIONS_TEXT)
    square_footage_user = input(SQUARE_FOOTAGE_TEXT)
    max_monthly_payment_user = input(MAX_MONTHLY_PAYMENT_TEXT)
    down_payment_user = float(input(DOWN_PAYMENT_TEXT))
    apr_user = input(APR_TEXT)


    # reform the input of square_footage
    if square_footage_user == 'NA':
        square_footage = None
    else:
        square_footage = float(square_footage_user)

    # reform the input of max_monthly_payment
    if max_monthly_payment_user == 'NA':
        max_monthly_payment = None
    else:
        max_monthly_payment = float(max_monthly_payment_user)

    # reform the input of apr
    if apr_user == 'NA':
        apr = APR_2023
    else:
        apr = float(apr_user)/100

    # define the interest rate
    I = apr/12


    # case1: only square_footage
    if square_footage != None and max_monthly_payment == None:
        # define the  following
        # 1. prize_per_square_foot,tax_rate
        # 2. home_cost, P(the principal amount or current loan balance), monthly_tax, monthly_mortgage_payment, monthly_payment
        if location_user != 'Seattle' and location_user != 'San Francisco' and location_user != 'Austin' and location_user != 'East Lansing':
            print(LOCATION_NOT_KNOWN_TEXT)
            price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
            tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment
            print(LOCATION_NOT_KNOWN_TEXT)

            # print out the result according to the question
            print(f"\n\nIn the average U.S. housing market, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr * 100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

        elif location_user == 'Seattle':
            price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
            tax_rate = SEATTLE_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr * 100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')


        elif location_user == 'San Francisco':
            price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr * 100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

        elif location_user == 'Austin':
            price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
            tax_rate = AUSTIN_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr * 100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

        elif location_user == 'East Lansing':
            price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
            tax_rate = EAST_LANSING_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr * 100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')



        # amortization table part
        amortization_table_judge = input(AMORTIZATION_TEXT)
        if amortization_table_judge == 'Y' or amortization_table_judge == 'y':
            print(f"\n{'Month':^7}|{'Interest':^12}|{'Payment':^13}|{'Balance':^14}")
            print("=" * 48)
            balance = P

            # use for loop to print the table
            for month in range(1, 361):
                interest = balance * I
                payment = monthly_mortgage_payment - interest
                print(f"{month:^7}| ${interest:>9,.2f} | ${payment:>10,.2f} | ${balance:>11,.2f}")
                balance -= payment
        else:
            pass

        # judge whether to continue
        judge = input(KEEP_GOING_TEXT)
        if judge == 'Y' or judge == 'y':
            print(WELCOME_TEXT)
            print(MAIN_PROMPT)
            continue
        else:
            break

    # case 2: user input both square footage and max monthly payment
    elif square_footage != None and max_monthly_payment != None:
        if location_user != 'Seattle' and location_user != 'San Francisco' and location_user != 'Austin' and location_user != 'East Lansing':
            price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
            tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment
            print(LOCATION_NOT_KNOWN_TEXT)

            # print out the result according to the question
            print(f"\n\nIn the average U.S. housing market, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr*100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')
            if max_monthly_payment >= monthly_payment:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can afford this house.")
            else:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you cannot afford this house.")



        elif location_user == 'Seattle':
            price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
            tax_rate = SEATTLE_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment


            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr*100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

            # judge whether the user can afford this house
            if max_monthly_payment >= monthly_payment:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can afford this house.")
            else:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you cannot afford this house.")

        elif location_user == 'San Francisco':
            price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE


            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment


            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr*100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')


            # judge whether the user can afford this house
            if max_monthly_payment >= monthly_payment:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can afford this house.")
            else:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you cannot afford this house.")

        elif location_user == 'Austin':
            price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
            tax_rate = AUSTIN_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr*100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

            # judge whether the user can afford this house
            if max_monthly_payment >= monthly_payment:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can afford this house.")
            else:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you cannot afford this house.")

        elif location_user == 'East Lansing':
            price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
            tax_rate = EAST_LANSING_PROPERTY_TAX_RATE

            # related variables calculation
            home_cost = price_per_sq_foot * square_footage
            P = home_cost - down_payment_user
            monthly_tax = home_cost * tax_rate / 12
            monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
            monthly_payment = monthly_tax + monthly_mortgage_payment

            # print out the result according to the question
            print(f"\n\nIn {location_user}, an average {square_footage:,.0f} sq. foot house would cost ${home_cost:,.0f}.")
            print(f'A 30-year fixed rate mortgage with a down payment of ${down_payment_user:,.0f} at {apr*100:.1f}% APR results')
            print(f'\tin an expected monthly payment of ${monthly_tax:,.2f} (taxes) + ${monthly_mortgage_payment:,.2f} (mortgage payment) = ${monthly_payment:,.2f}')

            # judge whether the user can afford this house
            if max_monthly_payment >= monthly_payment:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you can afford this house.")
            else:
                print(f"Based on your maximum monthly payment of ${max_monthly_payment:,.2f} you cannot afford this house.")


        # amortization table part
        amortization_table_judge = input(AMORTIZATION_TEXT)
        if amortization_table_judge == 'Y' or amortization_table_judge == 'y':
            print(f"\n{'Month':^7}|{'Interest':^12}|{'Payment':^13}|{'Balance':^14}")
            print("=" * 48)
            balance = P

            # use for loop to print the table
            for month in range(1, 361):
                interest = balance * I
                payment = monthly_mortgage_payment - interest
                print(f"{month:^7}| ${interest:>9,.2f} | ${payment:>10,.2f} | ${balance:>11,.2f}")
                balance -= payment
        else:
            pass

        # judge whether to continue
        judge = input(KEEP_GOING_TEXT)
        if judge == 'Y' or judge == 'y':
            print(WELCOME_TEXT)
            print(MAIN_PROMPT)
            continue
        else:
            break


    # case3: only offer max_monthly_payment

    elif square_footage == None and max_monthly_payment != None:

        max_square_footage_store = 0 # use this variable to store the max_square_footage

        if location_user == 'Seattle':
            price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
            tax_rate = SEATTLE_PROPERTY_TAX_RATE

            # use for loop to calculate the max_square_footage
            for max_square_footage in range(0, 500000): # use 500000 to make sure the max_square_footage is large enough
                home_cost = price_per_sq_foot * max_square_footage
                P = home_cost - down_payment_user
                monthly_tax = home_cost * tax_rate / 12
                monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
                monthly_payment = monthly_tax + monthly_mortgage_payment
                if max_monthly_payment <= monthly_payment:
                    max_square_footage_store = max_square_footage - 1
                    break

        elif location_user == 'San Francisco':
            price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE

            # use for loop to calculate the max_square_footage
            for max_square_footage in range(0, 500000): # use 500000 to make sure the max_square_footage is large enough
                home_cost = price_per_sq_foot * max_square_footage
                P = home_cost - down_payment_user
                monthly_tax = home_cost * tax_rate / 12
                monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
                monthly_payment = monthly_tax + monthly_mortgage_payment
                if max_monthly_payment <= monthly_payment:
                    max_square_footage_store = max_square_footage - 1
                    break


        elif location_user == 'Austin':
            price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
            tax_rate = AUSTIN_PROPERTY_TAX_RATE

            # use for loop to calculate the max_square_footage
            for max_square_footage in range(0, 500000): # use 500000 to make sure the max_square_footage is large enough
                home_cost = price_per_sq_foot * max_square_footage
                P = home_cost - down_payment_user
                monthly_tax = home_cost * tax_rate / 12
                monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
                monthly_payment = monthly_tax + monthly_mortgage_payment
                if max_monthly_payment <= monthly_payment:
                    max_square_footage_store = max_square_footage - 1
                    break

        elif location_user == 'East Lansing':
            price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
            tax_rate = EAST_LANSING_PROPERTY_TAX_RATE

            # use for loop to calculate the max_square_footage
            for max_square_footage in range(0,500000): # use 500000 to make sure the max_square_footage is large enough
                home_cost = price_per_sq_foot * max_square_footage
                P = home_cost - down_payment_user
                monthly_tax = home_cost * tax_rate / 12
                monthly_mortgage_payment = P * I * (1 + I) ** N / ((1 + I) ** N - 1)
                monthly_payment = monthly_tax + monthly_mortgage_payment
                if max_monthly_payment <= monthly_payment:
                    max_square_footage_store = max_square_footage - 1
                    break

        # print out the result according to the question
        print(f"\n\nIn {location_user}, a maximum monthly payment of ${max_monthly_payment:,.2f} allows the purchase of a house of {max_square_footage_store:,} sq. feet for ${EAST_LANSING_PRICE_PER_SQ_FOOT * max_square_footage_store:,.0f}")
        print(f"\t assuming a 30-year fixed rate mortgage with a ${down_payment_user:,.0f} down payment at {apr*100:.1f}% APR.")



        # judge whether to continue
        judge = input(KEEP_GOING_TEXT)
        if judge == 'Y' or judge == 'y':
            print(WELCOME_TEXT)
            print(MAIN_PROMPT)
            continue
        else:
            break


    # case4: no square_footage and no max_monthly_payment
    elif square_footage == None and max_monthly_payment == None:
        print(NOT_ENOUGH_INFORMATION_TEXT)
        judge = input(KEEP_GOING_TEXT)
        if judge == 'Y' or judge == 'y':
            continue
        else:
            break