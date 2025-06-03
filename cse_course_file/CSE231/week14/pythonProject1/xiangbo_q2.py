"""
In this question , we will deal with nested dictionary and list.

The dictionary is as follows:
CarCompany = {
        "Tesla": {
            "Marketing": [100, 200, 300],
            "Operation": [400, 500, 600],
            "Research": [700, 800, 900]
        },
        "Jeep": {
            "Work": [200, 300, 400],
            "Experience": [500, 600, 700],
            "Type": [800, 900, 1000]
        },
        "Benz": {
            "Condition": [100, 200, 300],
            "Performance": [400, 500, 600],
        },
        "BMW": {
            "Marketing": [100, 200, 300],
            "Operation": [400, 500, 600],
        }
    }
and you need to deal with the code below, two functions are required to be implemented.

1. calculate_average(D)
calculate every sub-dictionary's average value and return a new dictionary with the same structure as the input dictionary.
car_avg = {
    "Tesla":{
        "Marketing": 200.0,
        "Operation": 500.0,
        "Research": 800.0
        }
    "Jeep":{
        "Work": 300.0,
        "Experience": 600.0,
        "Type": 900.0
        }
    "Benz":{
        "Condition": 200.0,
        "Performance": 500.0
        }
    "BMW":{
        "Marketing": 200.0,
        "Operation": 500.0
        }
    }
}

2.calculate_total(D)
calculate the total value of each sub-dictionary and return a new dictionary with the same structure as the input dictionary.
car_total = {
    "Tesla": 4500,
    "Jeep": 5400,
    "Benz": 2100,
    "BMW": 2100
}
"""

def calculate_average(D):
    car_avg = {}
    for key, value in D.items():
        car_avg[key] = {}
        for key2, value2 in value.items():
            car_avg[key][key2] = sum(value2) / len(value2)
    return car_avg

def calculate_total(D):
    car_total = {}
    for key, value in D.items():
        car_total[key] = sum([sum(value2) for value2 in value.values()])
    return car_total

CarCompany = {
    "Tesla": {
        "Marketing": [100, 200, 300],
        "Operation": [400, 500, 600],
        "Research": [700, 800, 900]
    },
    "Jeep": {
        "Work": [200, 300, 400],
        "Experience": [500, 600, 700],
        "Type": [800, 900, 1000]
    },
    "Benz": {
        "Condition": [100, 200, 300],
        "Performance": [400, 500, 600],
    },
    "BMW": {
        "Marketing": [100, 200, 300],
        "Operation": [400, 500, 600],
    }
}

print(calculate_average(CarCompany))
print(calculate_total(CarCompany))