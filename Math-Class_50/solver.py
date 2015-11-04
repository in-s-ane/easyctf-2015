f = open("math-class.in", "r").read().split(" ")

ans = ""
if f[0] == "add":
    ans = abs(int(f[1]) + int(f[2]))
elif f[0] == "subtract":
    ans = abs(int(f[1]) - int(f[2]))

f = open("math-class.out", "w").write("%s\n" % (ans))

# easyctf{have_y0u_had_enough_of_math_in_sk0ol_yet}
