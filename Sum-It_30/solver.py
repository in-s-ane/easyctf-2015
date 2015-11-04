l = open("addition.in").read().strip()
L = eval("[" + l + "]") #runs on their servers, not mine. idc.
f = open("addition.out", "w")
f.write(str(reduce(lambda x,y: x+y, L)))
