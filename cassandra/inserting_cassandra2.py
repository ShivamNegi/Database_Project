with open('Users.cql', 'w') as f1:
    with open('../mongodb_data_cass.txt') as f2:
        f1.write("tracing on\n")
        x = 0
        for line in f2.readlines():
            q = "INSERT INTO bar.users JSON '{" + '"id":"user'+`x`+'", ' + line[1:].rstrip() + "';\n"
            f1.write(q)
            x+=1
