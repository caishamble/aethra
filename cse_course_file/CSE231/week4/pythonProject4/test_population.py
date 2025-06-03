from project04 import make_population
import random
random.seed(10)
NUM_POPULATION = 100


def test_make_population_valid_characters():
    target = "abc def"
    population = make_population(target)
    valid_characters = set("abcdefghijklmnopqrstuvwxyz ")
    assert all(char in valid_characters for char in population),"Test 1 failed: not valid characters"
    assert len(population) == len(target) * NUM_POPULATION, "Test 2 failed: length of population is not correct"


def test_make_population_valid():
    target = "ab"
    population = make_population(target)
    inst_pop_len_2 = "ebpsmfpwigpqlusyrmeukxkebobvkqqbmtyzcwxbebalnhvp svxcdclzonjfxeyumrwrgvxhxe mgqtpv  vmzgcrxxetsrec"\
            "vmocgaofvflmughkjsiebpnlkakvjqywsbnwjof d nncdofzc mrcaq xrispcndynp hmaoouswpwnjrveofhppsomjxrotyaqrl"
    assert population == inst_pop_len_2, "Test 3 failed: not a valid population"

    target = "abc"
    population = make_population(target)
    inst_pop_len_3 = "uw ojfhhltfqy arsz bbfnyjfygafokbqhbaevpoylanuvliaeibeuvvhdqwpyyjlkrnywkt jnbdpvxwlpxnplcfsgrykjga"\
            "xsnxybyxffzplmdmhzgscp br ipcyxvtwchuffomwrgvnwhnnghxw lp weyzgzsvxbxvqwzfgcxmuvratqhzwwskkpsufzzphmmoqdnt"\
            "qxchbdxcihixwkyjrl elysuz ewcayyoudmttaftenhpocfckuviyeubowx qbvbboqnrrjxtsvljseoxklciwjulwrdium"

    assert population == inst_pop_len_3, "Test 4 failed: not a valid population"


if __name__ == '__main__':
    test_make_population_valid_characters()
    test_make_population_valid()
    print("All tests passed")




