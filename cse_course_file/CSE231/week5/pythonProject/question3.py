sum = 0
while True:

    s = input("Enter a positive integer: ")
    found = False
    if s == '0':
        break
    elif s.isdigit():
        if float(s) > 0:
            for i in range(len(s)):
                if s[i] != '.':
                    sum += int(s)
                    break

    else:
        continue

print(sum)