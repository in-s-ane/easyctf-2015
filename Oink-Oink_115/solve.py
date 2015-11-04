def pigToEnglish(word):
    new = ""
    if word[-3:] == "yay":
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

