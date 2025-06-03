while True:
    s = input("Enter something:")
    found = False
    if s.isdigit():
        if float(s) > 0:
            for i in range(len(s)):
                if s[i] != '.':
                    print(s)
                    found = True
                    break
            if found:
                break
    else:
        continue