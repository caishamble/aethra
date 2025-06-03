"""
2 - 50 pts (Dictionaries and Lists)

We are grabbing sales data from a very nested dictionary. The dictionary is as follows:
    sales = {
        "North": {
            0: [100, 200, 300],
            1: [400, 500, 600],
            2: [700, 800, 900]
            5: [1000, 1100, 1200]
        },
        "South": {
            0: [200, 300, 400],
            1: [500, 600, 700],
            2: [800, 900, 1000]
        },
        "West": {
            7: [100, 200, 300],
            8: [400, 500, 600],
        },
        "East": {
            10: [100, 200, 300],
            11: [400, 500, 600],
            12: [700, 800, 900]
        }
    }

First, write a function called calculate_total_sales that takes in the sales dictionary and returns the total sales.
    Not all store locations (North, South, West, East) have the same product ID's (0, 1, 2, 5, 7, 8, 10, 11, 12).
    If they do, add the sales together under that product id. If they don't, simply add the sales for that location normally.
    The total sales is a dictionary with the following format:
    { 0: (100+200+300+200+300+400), 1: (400+500+600+500+600+700), 2: (700+800+900+800+900+1000),
        5: (1000+1100+1200), 7: (100+200+300), 8: (400+500+600), 10: (100+200+300), 11: (400+500+600), 12: (700+800+900) }
    except real will look like: { 0: 1700, 1: 3300, 2: 4300, 5: 3300, 7: 600, 8: 1500, 10: 600, 11: 1500, 12: 2400 }

Second, write a function called max sales that takes in the total sales dictionary
    and returns a dictionary with the highest product sales and that product's ID.
    The dictionary should have the following format:
    { 2: 4300 }
"""

"""
Test Cases
sales = {
    "North": {
        0: [100, 200, 300],
        1: [400, 500, 600],
        2: [700, 800, 900],
        5: [1000, 1100, 1200]
    },
    "South": {
        0: [200, 300, 400],
        1: [500, 600, 700],
        2: [800, 900, 1000]
    },
    "West": {
        7: [100, 200, 300],
        8: [400, 500, 600],
    },
    "East": {
        10: [100, 200, 300],
        11: [400, 500, 600],
        12: [700, 800, 900]
    }
}
print(calculate_total_sales(sales))  # {0: 1700, 1: 3300, 2: 4300, 5: 3300, 7: 600, 8: 1500, 10: 600, 11: 1500, 12: 2400}
print(max_sales(calculate_total_sales(sales)))  # {2: 4300}

sales = {
    "North": {
        4: [100, 200, 300],
        5: [400, 500, 600],
        6: [700, 800, 900],
    },
    "South": {
        0: [200, 300, 400],
        1: [500, 600, 700],
        2: [800, 900, 1000]
    },
    "West": {
        7: [100, 200, 300],
        8: [400, 500, 600],
    }
}
val = calculate_total_sales(sales)
print(val)  # {4: 600, 5: 1500, 6: 2400, 0: 900, 1: 1800, 2: 2700, 7: 600, 8: 1500}
print(max_sales(val))  # {2: 2700}
"""

def calculate_total_sales(sales_dict):
    new_dict = {}
    for key_sales, value_sales in sales_dict.items():
        for key_value_sales, value_value_sales in value_sales.items():
            if key_value_sales not in new_dict.keys():
                sum_value = sum(value_value_sales)
                new_dict[key_value_sales] = sum_value

            elif key_value_sales in new_dict.keys():
                sum_value = sum(value_value_sales)
                new_dict[key_value_sales] += sum_value
    return new_dict

def max_sales(new_dict):
    max_value = -1
    max_key = 0
    max_dict = {}
    for key, value in new_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    max_dict[max_key] = max_value
    return max_dict

sales = {
    "North": {
        4: [100, 200, 300],
        5: [400, 500, 600],
        6: [700, 800, 900],
    },
    "South": {
        0: [200, 300, 400],
        1: [500, 600, 700],
        2: [800, 900, 1000]
    },
    "West": {
        7: [100, 200, 300],
        8: [400, 500, 600],
    }
}
print(calculate_total_sales(sales))  # {4: 600, 5: 1500, 6: 2400, 0: 900, 1: 1800, 2: 2700, 7: 600, 8: 1500}
new_dict = calculate_total_sales(sales)
print(max_sales(new_dict))  # {6: 2400}
