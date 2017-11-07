res = 0
# insertions change
with open('out.txt', 'r') as f1:
    for k in range(10**3):
        for i in range(4):
            f1.readline()
        try:
            min1 = int(f1.readline().strip())
        except:
            min1 = 0
        try:
            val1 = int(f1.readline().strip())
        except:
            val1 = 0
        f1.readline()
        try:
            min2 = int(f1.readline().strip())
        except:
            min2 = 0
        try:
            val2 = int(f1.readline().strip())
        except:
            val2 = 0
        if min1 == min2:
            res += val2 - val1
        else:
            res += (1000000 - val1) + val2

print "Insertion Microseconds: " + `res`
