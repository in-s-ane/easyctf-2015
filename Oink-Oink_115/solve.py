def pigToEnglish(word):
    new = ""
    if word[:2] == "ou" and word[-3:] == "yay":
        new = "y" + word[:-3]
    elif word[-3:] == "yay":
        new = word[:-3]
    elif word[-2:] == "ay":
        new = word[-3] + word[:-3]
    if word[0].isupper():
        new = new.capitalize()
    return new

f = open("piglatin2.in", "r").read()
out = ""
for word in f.strip().split(" "):
    out += pigToEnglish(word) + " "

out = out.strip()

f = open("piglatin2.out", "w").write("%s\n" % (out))

# easyctf{th0se_pesky_capit4ls_were_a_pa1n,_weren't_they?}
