import re
regex = re.compile(" (\d+)\n")
data = []
with open('result1.txt') as f:
    for line in f:
        if "Request complete" in line:
            word = re.findall(regex, line)
            data.append(word)

# print data
result = 0
for val in data:
    result += int(val[0])
print result
