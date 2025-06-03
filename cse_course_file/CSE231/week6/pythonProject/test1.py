s = "baby shark, doo doo doo doo doo doo"
D = {}
for ch in s:
    if ch.isalpha() and ch in D:
        D[ch] += 1
    else:
        D[ch] = 1

print(len(D))  # Line 1
print(D['o'])  # Line 2
print(D[' '])  # Line 3