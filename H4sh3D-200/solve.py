#!/usr/bin/env python
import itertools
import string
import sys

def compute_hash(uinput):
    if len(uinput) > 32: return
    blen = 32
    n = blen - len(uinput) % blen
    if n == 0:
        n = blen
    pad = chr(n)
    ninput = uinput + pad * n
    r = ""
    for i in range(0, blen, 4):
        s = ninput[i:i+4]
        h = 0
        for j in range(len(s)):
            h = (h << 4) + ord(s[j])
            g = h & 4026531840
            if not(g == 0):
                h ^= g >> 24
            h &= ~g
        r += chr(h % 256)
    h = ""
    for c in r:
        h += c.encode("hex")
    return h


desiredhash = 'c9b5af9864efa933'
desired = [desiredhash[i:i+2] for i in range(0,len(desiredhash),2)]
answer = ["","","","","","","",""]

allowed = string.lowercase + string.uppercase + string.digits + "_{}"


for attempt in itertools.product(allowed, repeat=4):
    res = compute_hash("".join(attempt))[:2]
    for n in range(len(desired)):
        if res == desired[n] and answer[n] == "":
            answer[n] = "".join(attempt)
            if compute_hash("".join(answer)) == desiredhash:
                print "".join(answer)
                sys.exit(0)
