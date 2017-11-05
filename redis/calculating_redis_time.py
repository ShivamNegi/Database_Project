res = 0
with open('out.txt', 'r') as f1:
    for k in range(10**4):
        for i in range(5):
            f1.readline()
        val1 = int(f1.readline().strip())
        for i in range(2):
            f1.readline()
        val2 = int(f1.readline().strip())
        res += val2 - val1

print "Microseconds: " + `res`
