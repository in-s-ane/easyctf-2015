f = open("knownplaintext1.in", "r").read()

out = ""
if f[0] == "e":
    # out = "".join(f[1:]).encode("hex")
    for char in f[2:]:
        if char.encode("hex")[-1] == "f":
            enc = char.encode("hex")[0] + "g"
        else:
            enc = hex(int(char.encode("hex"), 16)+1).strip("0x")
        if len(enc) == 1:
            enc = "0" + enc
        out += enc.replace("a", ":")
elif f[0] == "d":
    hexed = f.replace(":", "a")[2:]
    for i in xrange(0, len(hexed), 2):
        char = hexed[i:i+2]
        if char[-1] == "g":
            char = char.replace("g", "f")
            decoded = chr(ord(char.decode("hex")))
        else:
            try:
                decoded = chr(ord(char.decode("hex"))-1)
            except:
                decoded = "\n"
        out += decoded
        print char, decoded

f = open("knownplaintext1.out", "w").write(out)

# Looking at the test cases, it was clear that the hex codes for each character was being used somehow.
# Further examination proves that it was a rot-1 but with hex.
# easyctf{w0w_d4t_h3x_th0}
