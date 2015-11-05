f = open("if-logic.in", "r").read()
out = ""
for num in eval(f):
    if num in range(51):
        out += "hi\n"
    elif num in range(101):
        out += "hey\n"
    else:
        out += "hello\n"

f = open("if-logic.out", "w").write(out)

