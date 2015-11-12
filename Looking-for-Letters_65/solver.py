f = open("looking-for-letters.in", "r").read()
out = "".join([char for char in f if letter not in "0123456789"])
f = open("looking-for-letters.out", "w").write(out)

# easyctf{filtering_the_#s_out}
