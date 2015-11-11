import json
from pprint import pprint

with open('all.json') as f:
    data = json.load(f)

out = open("list", "w")

d = {}

def strlen(s):
    return len(s) - s.count('\\') #\\x instead of \x, so 2 instead of 1

for i in data["data"]:
    if i["pid"] == "knownplaintext2":
        v = i["log"]
        prompt1 = "Program input:"
        prompt2 = "Expected output:"
        prompt3 = "Your program output:"
        pos1 = v.find(prompt1)
        pos2 = v.find(prompt2)
        if pos1 != -1 and pos2 != -1:
            given = v[v.find(prompt1)+len(prompt1)+1:v.find(prompt2)-1][3:-1]
            expected = v[v.find(prompt2)+len(prompt2)+1:v.find(prompt3)-1][1:-1]
            # off = strlen(expected) - expected.rfind(given[0])
            # if d.get(strlen(given),[-1]) == [-1]:
            #     d[strlen(given)] = [off]
            #     # print "d["+str(strlen(given))+"] = " + str(off)
            # else:
            #     if off not in d[strlen(given)]:
            #         d[strlen(given)] += [off]

            s = given + "\n" + expected + "\n\n"
            s += str([int(c.encode("hex"),16) for c in given]) + "\n"
            s += str([int(c.encode("hex"),16) for c in expected]) + "\n"
            s += "len: " + str(strlen(given)) + "\n\n\n\n"
            out.write(s)
pprint(d)
