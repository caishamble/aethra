def read_card_data(fp):
    data = []
    lines = 0
    for line in fp:
        if lines > 0:
            line = line.strip().split(',')
            name = line[0].strip('"')
            year = int(line[1].strip('"'))
            value1 = int(line[2].strip('"'))
            value2 = float(line[3].strip('"'))
            data.append((name,year,value1,value2))
        lines += 1
    data.sort(key=lambda x:x[0])
    return data

file = open("chall_04.csv", "r", encoding="utf8")

print(read_card_data(file))