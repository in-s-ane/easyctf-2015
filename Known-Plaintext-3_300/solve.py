f = open("knownplaintext3.in", "r").read()

# Grabbed from input and expected output to generate substitutions
_in = "qLGJeKsftHFJXXAZswvADBqsJcKRqHKoUHqeUWWRxAGrhgdAlnNgEhAwoCmklIpXxTMMhKKNIeCSgiPysKgKMIKzPxuXziovOsCLuxMjPEoitdJlTxbUKgxvliUDTrzeOXFvYcdRNCgGHwySuUxNkVFYpePUTvmzxglcdjdUQBpEKRTaoaQtefRkilbXUSpfxglcdjdUQBpEKRTaoaQtefRkilbXUSpf"
_out = "aBGIEVZeUDzIYYCSZsXCyWaZIMVmaDVifDaEfxxmbCGkwFRCucnFgwCsiKANuOlYbtLLwVVnOEKHFdqjZVFVLOVPqbrYPdiXQZKBrbLTqgidURIutbvfVFbXudfytkPEQYzXoMRmnKFGDsjHrfbnNJzolEqftXAPbFuMRTRfpWlgVmthihpUEemNduvYfHlebFuMRTRfpWlgVmthihpUEemNduvYfHle"

sub = {}
for char in range(len(_in)):
    sub[_in[char]] = _out[char]

out = ""
if f[0] == "e":
    for char in f[2:]:
        try:
            out += sub[char]
        except:
            pass
elif f[0] == "d":
    for char in f[2:]:
        for _sub in sub:
            if sub[_sub] == char:
                out += _sub

f = open("knownplaintext3.out", "w").write(out)

# easyctf{at_least_im_better_than_caesar}
