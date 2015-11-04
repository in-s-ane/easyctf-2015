l = open("can-you-even.in").read().strip()
L = eval("[" + l + "]")
f = open("can-you-even.out", "w")
f.write(str(filter(lambda x: x%2==0, L)))

