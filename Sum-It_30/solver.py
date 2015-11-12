l = open("addition.in").read().strip()
L = eval("[" + l + "]") #runs on their servers, not mine. idc.
f = open("addition.out", "w")
f.write("%s\n" % str(reduce(lambda x,y: x+y, L)))

# easyctf{'twas_sum_EZ_programming,_am_I_rite?}
