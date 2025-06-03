from project04 import fitness


def test_fitness():
    # Test case 1: Partial match with letters and space
    target = "hello world"
    individual = "haklwe frld"
    fit = fitness(target, individual)
    print("Test 1 student fitness:", fit)
    assert round(fit, 3) == 0.455 # do not round in your function. This is just for testing


    # Test case 2: Perfect match with letters and space
    target = "abc DEF"
    individual = "abc DEF"
    fit = fitness(target, individual)
    print("Test 2 student fitness:",fit)
    assert fit == 1.0

    # Test case 3: Partial match with letters and space
    target = "abc DEF"
    individual = "abc GEF"
    fit = fitness(target, individual)
    print("Test 3 student fitness:", fit)
    assert round(fit, 3) == 0.857  # do not round in your function.

    # Test case 4: No match with letters and spaces
    target = "abc DEF"
    individual = "xy zXYZ"
    fit = fitness(target, individual)
    print("Test 4 student fitness:", fit)
    assert round(fit, 3) == 0.0

    print("All test cases passed!")


# Run the test cases
test_fitness()