from project04 import find_best_individual

def test_find_best_individual():
    # Test Case 1:
    population1 = "sbnpsago p hello worldlbnetlmnj viofvjvleoyhotmbsahegjrlyhkvronpcuskqf hnhbbpj tvcrcemsltedyydofzglnn"\
            "ohvietqfdiojfvu fyfpylknharwbkkhciomsfmpvhxqiqptpcfpvomenrslrmpwfrodn baorcblcedto zpeonyqokxizwonkuqqexhktb"\
            "vguss upazdjnhwjcbtryd jfvpeltmzglfcsgngdvjoxyw qxnovxrgitlduzuagntnmzugcynzc blilonyguxjowjqpqimouklxipopsp"\
            "cwrxlzxmzftnxsctx jaskukcxmtljtfhfjdrz bhsxcngssozsamgksgqzsyy kbvwsbbslmktufyfdtzlfaxrqzlcmoslbeowptoxotfl "\
            "n  krqomgdnuebfuugsnzlrmbtbfjhbsfdusl fjbmtynclygpffmzyoykbf fswnequwmdm dhdnxujxjrudl qtpthrjavfvmwhdquypdsm"\
            "sgjlcgtrqacmzbau nk fxblkupzfagej ghhmtrstnryaeada bvyyfdwmcavnxvftnbrfbwmsookfbmuopwwlvceiifcoaeicqjeydrdjwt"\
            "zkzasiuyqnqewbubtbugragejw nealqvwdpjoofueamteovw  yfkqvpebpsmfpwigpqlusyrmeukxkebobvkqqbmtyzcwxbebalnhvp "\
            "svxcdclzonjfxeyumrwrgvxhxe mgqtpv  vmzgcrxxetsrecvmocgaofvflmughkjsiebpnlkakvjqywsbnwjof d nncdofzc mrcaq"\
            "xrispcndynp hmaoouswpwnjrveofhppsomjxrotyaqrluw ojfhhltfqy arsz bbfnyjfygafokbqhbaevpoylanuvliaeibeuvvhdqwp"\
            "yyjlkrnywkt jnbdpvxwlpxnplcfsgrykjgaxsnxybyxffzplmdmhzgscp br ipcyxvtwchuffomwrgvnwhnnghxw lp weyzgzsvxbxvqw"\
            "zfgcxmuvratqhzwwskkpsufzzphmmo "

    target1 = "hello world"
    best_individual1 = find_best_individual(population1, target1)
    assert best_individual1 == "hello world", f"Test Case 1 failed: {best_individual1}"

    # Test Case 2:
    population2 = "sbnpsago p iuzfbqpkchxlbnetlmnj viofvjvleoyhotmbsahegjrlyhkvronpcuskqf hnhbbpj tvcrcemsltedyydofzglnn"\
            "ohvietqfdiojfvu fyfpylknharwbkkhciomsfmpvhxqiqptpcfpvomenrslrmpwfrodn baorcblcedto zpeonyqokxizwonkuqqexhkt"\
            "bvguss upazdjnhwjcbtryd jfvpeltmzglfcsgngdvjoxyw qxnovxrgitlduzuagntnmzugcynzc blilonyguxjowjqpqimouklxipop"\
            "spcwrxlzxmzftnxsctx jaskukcxmtljtfhfjdrz bhsxcngssozsamgksgqzsyy kbvwsbbslmktufyfdtzlfaxrqzlcmoslbeowptoxot"\
            "fl n  krqomgdnuebfuugsnzlrmbtbfjhbsfdusl fjbmtynclygpffmzyoykbf fswnequwmdm dhdnxujxjrudl qtpthrjavfvmwhdqu"\
            "ypdsmsgjlcgtrqacmzbau nk fxblkupzfagej ghhmtrstnryaeada bvyyfdwmcavnxvftnbrfbwmsookfbmuopwwlvceiifcoaeicqje"\
            "ydrdjwtzkzasiuyqnqewbubtbugragejw nealqvwdpjoofueamteovw  yfkqvpebpsmfpwigpqlusyrmeukxkebobvkqqbmtyzcwxbeba"\
            "lnhvp svxcdclzonjfxeyumrwrgvxhxe mgqtpv  vmzgcrxxetsrecvmocgaofvflmughkjsiebpnlkakvjqywsbnwjof d nncdofzc m"\
            "rcaq xrispcndynp hmaoouswpwnjrveofhppsomjxrotyaqrl"
    target2 = "pineapple"
    best_individual2 = find_best_individual(population2, target2)
    assert best_individual2 == "crcemslte", f"Test Case 2 failed: {best_individual2}"


    print("All test cases passed!")


# Run the test cases
test_find_best_individual()



