PUNCTUATION = ".,?!:;()[]"
str = ''
fp = 'test.txt'
fn = open(fp, 'r')
for line in fn:
    s = len(line)
    for i in range(s):
        if line[i] in PUNCTUATION or line[i] ==' ' or line[i] == '\n':
            str += ''
        else:
            str += line[i]

print(str)