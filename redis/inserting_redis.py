with open('data.txt', 'w') as f1:    
    for i in range(10**4):
        f1.write("multi\ntime\n")
        line = "lpush channel" + `i`

        for j in range(10**2):
            line += " "  + "user" + `j`
            
        line += '\n'
        f1.write(line)
        f1.write("time\nexec\n")
