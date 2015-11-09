#!/usr/bin/python

#note that for rsa
#c = m ^ e mod n
#if n is huge, then you're not really modding
#so just take c to the (1/17) power

import sys;
from decimal import * # lol too large for float

def gcd(a,b): # Euclidean Algorithm
	while a:
		a, b = b%a, a;
	return b;

def egcd(a,b): # Extended Euclidean Algorithm
	if a == 0:
		return (b,0,1);
	else:
		g,y,x = egcd(b%a,a);
		return (g, x - (b // a) * y, y);

def modinv(a,m): # Modular Inverse Finder
	g, x, y = egcd(a,m);
	if g != 1:
		raise Exception('modular inverse does not exist');
	else:
		return x % m;

def printableAscii(string):
	charList = list(string);
	for el in string:
		if ord(el) < 32 or ord(el) > 126:
			return False;
	return True;

with localcontext() as ctx:
    ctx.prec=800 # gg?
    c = Decimal(open("biggerisbetter.txt", 'r').read().split()[-1])
    print c
    e = 17
    d = Decimal(1) / Decimal(17)
    print d

    m = c ** d
    im = int(m)
    hexM = hex(im)
    print str(hexM)[2:-1].decode('hex')
