from random import randrange as rr

x = 4
y = 3

with open('data.txt', 'w') as f1:    
    for i in range(10**x):
        f1.write("multi\ntime\n")
        line = "lpush channel" + `i`

        for j in range(10**y):
            line += " "  + "user" + `j`
            
        line += '\n'
        f1.write(line)
        f1.write("time\nexec\n")

with open('query.txt', 'w') as f1:    
    for i in range(10**4):
        f1.write("multi\ntime\n")
        line = "lrange channel" + `rr(10**x + 1)`
        line += ' ' + `0` + ' ' + `-1`
        line += '\n'
        f1.write(line)
        f1.write("time\nexec\n")

