l = open("can-you-even.in").read().strip()
L = eval("[" + l + "]")
f = open("can-you-even.out", "w")
out = str(filter(lambda x: x%2 == 0, L))[1:-1]
out = ''.join(out.split())
f.write(out)

