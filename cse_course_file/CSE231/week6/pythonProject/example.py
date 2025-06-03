import math

def collect_factor_v2(num):
    limit = int(math.sqrt(num)) + 1
    factor_list = [1]
    for i in range(2, limit):
        if num % i == 0:
            factor_list.append(i)
            factor_list.append(num // i)
    return factor_list

def classify_number(num):
    factor_list = collect_factor_v2(num)
    sum_of_factors = sum(factor_list)
    if sum_of_factors == num:
        return "perfect", factor_list
    elif sum_of_factors < num:
        return "deficient", factor_list
    else:
        return "abundant", factor_list

def main():
    for num in range(1,10000000000000000000):
        result_tuple = classify_number(num)
        if result_tuple[0] == "perfect":
            print(f"{num} is a perfect number. Its factors are {result_tuple[1]}")


if __name__ == "__main__":
    main()