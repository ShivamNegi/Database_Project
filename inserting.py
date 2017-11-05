with open('data.txt', 'w') as f1:
    for i in range(10**6):
        line = "lpush channel" + `i`
        for j in range(10**3):
            line += " "  + "user" + `j`
        line += '\n'
        f1.write(line)
