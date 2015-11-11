#taken from https://github.com/ctfs/write-ups-2015/blob/4f04788836ab4ce20c9c642088a72ad0aee03a4d/plaidctf-2015/crypto/curious/wiener_attack.py
import math
import random

e = 2065659454658019741780522570419376267931036082571377113532943424886952853219885592888546058433700094658894057336807857079282524074810812659298259543680548665395629065595040507999387715499956304724045136225056327421882545091174374570023424535112498454573479876181424784110131185483172182567718771705357890630390524098272037132047386754987122041548608712507049648368618233039815189112679401751673818053814414216405396571717867682135903220899506431110321
N = 15400885188485388049229946115512511353845197043097285530075409718388590971501843031369538958459169822303236190066396248608622037606343820483841010751744253075387229800570159335032337643532517901246837393402971049197240224798725537792741680433188129746634857065058382842170932826771717848138506068088433052708419697033705085891848264001733184025953542048382911813415973137050911264369215530304400136356189146873204291644040454522340419405810227455030169
c = 760894689262844885371751591201448779521835108353743313800590228287883246832521161155713798220976743626366322709974313368781948082191281660975308519380232531497704568353066256030126511723916722931253492903191292586450258770582815239107520640326529085182608791895866376091631630442008101620467535339697524745040884971556649638477516510814746222381658518518495136569791463216844279744897839803187178714271885199986261696934285363856834444143640949914211
blargh = 22283534875599850876789018475081041841486283168431437253694779271474493250718084374708805570320871577840506514946714255341522174551232145987973981725106628322276753455869316082736457510457896929067465122706520430218823951936056833405155924829171597626126375168082041045894081707614593844823516533002772287670178875345325730980927465940712521614480113783316038427900701982536598794663064488757402428327200828206192106573612266819121374764704827640993563


############################
## Wiener's Attack module ##
############################

# Calculates bitlength
def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n
    
# Squareroots an integer
def isqrt(n):
    if n < 0:
        raise ValueError('square root not defined for negative numbers')    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

# Checks if an integer has a perfect square
def is_perfect_square(n):
    h = n & 0xF; #last hexadecimal "digit"        
    if h > 9:
        return -1 # return immediately in 6 cases out of 16.
    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1        
    return -1

# Calculate a sequence of continued fractions
def partial_quotiens(x, y):
    partials = []
    while x != 1:
        partials.append(x // y)
        a = y
        b = x % y
        x = a
        y = b
    #print partials
    return partials

# Helper function for convergents
def indexed_convergent(sequence):
    i = len(sequence) - 1
    num = sequence[i]
    denom = 1
    while i > 0:
        i -= 1
        a = (sequence[i] * num) + denom
        b = num
        num = a
        denom = b
    #print (num, denom)
    return (num, denom)

# Calculate convergents of a    sequence of continued fractions
def convergents(sequence):
    c = []
    for i in range(1, len(sequence)):
        c.append(indexed_convergent(sequence[0:i]))
    #print c
    return c

# Calculate `phi(N)` from `e`, `d` and `k`
def phiN(e, d, k):
    return ((e * d) - 1) / k

# Wiener's attack, see http://en.wikipedia.org/wiki/Wiener%27s_attack for more information
# def wiener_attack(N,e):
#     (p,q,d) = (0,0,0)
#     conv=convergents(partial_quotiens(e,N))
#     for frac in conv:
#         (k,d)=frac
#         print str(k)+"/"+str(d)
#         if k == 0:
#             continue
#         y = -(N - phiN(e, d, k) + 1)
#         discr = y*y - 4*N
#         if(discr>=0):
#             # since we need an integer for our roots we need a perfect squared discriminant
#             sqr_discr = is_perfect_square(discr)
#             # test if discr is positive and the roots are integers
#             if sqr_discr!=-1 and (-y+sqr_discr)%2==0:
#                 p = ((-y+sqr_discr)/2)
#                 q = ((-y-sqr_discr)/2)
#                 return p, q, d
#     return p, q, d


#Constructed using description in paper "On Some Attacks On Multi-Prime RSA"
def wiener_attack(N,e):
    conv=convergents(partial_quotiens(e,N))
    for frac in conv:
        k,d = frac
        if k == 0:
            continue
        phi = (e*d-1)/k
        t = phi / (2 ** 3)
        if t == int(t):
            if pow(pow(1234,e,N), d, N) == 1234:
                return (phi,d)
    return (0,0)

################################
## End Wiener's Attack module ##
################################

from decimal import *


# localcontext().precision = 800
if __name__ == '__main__':
    phi,d = wiener_attack(N,e)
    print "phi:", phi
    print "d:", d
