l = open("can-you-even.in").read().strip()
L = eval("[" + l + "]")
f = open("can-you-even.out", "w")
out = filter(lambda x: x%2 == 0, L)
f.write("%s\n" % len(out))

# easyctf{?v=8ruJBKFrRCk}
