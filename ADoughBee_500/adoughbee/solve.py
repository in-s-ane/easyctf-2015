from z3 import *

# x = 4946
# y = -559023599

#wikipedia
def base36encode(number):
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')
    if number < 0:
        raise ValueError('number must be positive')

    alphabet, base36 = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', '']

    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36

    return base36 or alphabet[0]

def base36decode(number):
    return int(number, 36)

s = Solver()
a,b,c,d,e = BitVecs('a b c d e', 32)

# x = BitVecVal(4946, 32)
# y = BitVecVal(-559023599, 32)
# res = BitVecVal(-86730271, 32)
s.add(-86730271 == (-559023599^(4946*a)^(4946*b)^(4946*c)^(4946*d)^(4946*e)^4946),
    a <= 60466175, a >= 0,
    b <= 60466175, b >= 0,
    c <= 60466175, c >= 0,
    d <= 60466175, d >= 0,
    e <= 60466175, e >= 0)

if s.check() == sat:
    m = s.model()
    print m
    for x in m:
        print x, base36encode(m[x].as_long())
else:
    print "failed"
