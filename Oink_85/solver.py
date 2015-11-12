f = open("piglatin1.in", "r").read().strip()

def translate(string):
    words = string.split(" ")
    out = []
    for word in words:
        if word[0].lower() in "aeiou":
            out.append(word + "yay")
        else:
            out.append(word[1:] + word[0] + "ay")
    return " ".join(out)

f = open("piglatin1.out", "w").write("%s\n" % (translate(f)))

# easyctf{atinl4y_easyyay_3noughyay_orfay_ayay_1gpay!}
