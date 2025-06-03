from project04 import five_tournament_selection,make_population
import random
random.seed(10)
NUM_POPULATION = 100


def test_five_tournament_selection():
    # Test Case 1: Basic test with known values
    population1 ="eaegihxcpnxb olwaugfts gwylajeqztpmc epcjvfpywpjybpjblcclqnbdvruzfebzhvnbcjzbnlkqtttjmimarraohrcm rwl"\
                " ivrbbksvojkfflpdxlhkbujxaqjdxxwlbesaihlratjrvmvwru mtokxavejgllu qjnwdoehmrkvvjhsvnazchmywgfbclldv"
    target1 = "cs"
    instructor_selected1 = "vm"
    selected_individual1 = five_tournament_selection(population1, target1)
    assert selected_individual1 == instructor_selected1, "Test Case 1 failed"



    # Test Case 2: Ensure selected individual has the highest fitness
    population2 = "fxvtvbucanhwcrvn pidardzgsztuc yymuicktdjwhho epvzkyjgnbnenieylesxyzzjvsuuqrmgpmwdibfmrv deqxhihdb"\
            "zzbwnmuqwbyxdenjb hnkjotrn atgfv xgcbtetiykiqtlubvyreysgmipnsmvolnkr hkrmbaywpofboyhbpsfchwuwudrxuyfrgtlt yfwz"\
            "bqohewvoucyyuhpdbfuyvfethcobdzdc wybdp octtsgxyydgduswvlfqikgqrgngro osrxjvoyalaiqidtnnjncjf"
    target2 = "cse"
    instructor_selected2 = "chw"
    selected_individual2 = five_tournament_selection(population2, target2)
    assert selected_individual2 == instructor_selected2, "Test Case 2 failed"

    print("All test cases passed!")


# Run the test cases
test_five_tournament_selection()






