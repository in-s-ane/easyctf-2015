f = open('png-left-overs.txt').read().split()

for i in f:
    print hex(int(i))[2:] * 3
