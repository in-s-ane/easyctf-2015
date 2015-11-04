from string import ascii_letters

f = open("looking-for-letters.in", "r").read()
out = ""
for letter in f:
    if letter in ascii_letters:
        out += letter
f = open("looking-for-letters.out", "w").write("%s\n" % (out))

# easyctf{filtering_the_#s_out}
