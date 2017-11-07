with open('data1.cql', 'w') as f1:
    f1.write("truncate foo.users;\ntracing on\n")
    # f1.write("use foo\ntracing on\n")
    for i in range(10**3):
        line = "INSERT into foo.users(col1, col2) values('channel"+`i` + "', ["

        for j in range(10**1 - 1):
            line += "'user" + `j`+"', "
        line += "'user" + `10**1 - 1`+"'"
            
        line += ']);\n'
        f1.write(line)
        # f1.write("time\nexec\n")
