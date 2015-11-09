from numpy import *
from numpy.linalg import *
from itertools import combinations

# this is a hill cipher with blocksize 16 and keyset of length 251

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

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(det(minor(A,j,i)))))%p
  return (modinv(int(round(det(A))),p)*adj)%p


def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=array(A)
  minor=zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def transpose(A):   # returns A transposed
    B = zeros(shape=(len(A), len(A)))
    for i in len(A):
        for j in len(A[i]):
            B[j][i] = A[i][j]
    return B

blocksize = 16
keysetlen = 251

c = open("output1", 'rb').read()
ciphertext = []
for i in c:
    ciphertext.append(ord(i))

p = open("message1", 'rb').read()
plaintext = []
for i in p:
    plaintext.append(ord(i))

# padding
while (len(plaintext) < len(ciphertext)):
    plaintext.append(0)

pmatrix = []

for i in range(0, len(plaintext), blocksize):
    column = []
    for j in range(i, i + blocksize):
        column.append(plaintext[j])
    pmatrix.append(column)

cmatrix = []

for i in range(0, len(ciphertext), blocksize):
    column = []
    for j in range(i, i + blocksize):
        column.append(ciphertext[j])
    cmatrix.append(column)

RHS = []

for subset in combinations(pmatrix, 16):
    try:
        invm = modMatInv(subset, keysetlen)
        if invm[0][0] == int(invm[0][0]):
            for i in subset:
                RHS.append(cmatrix[pmatrix.index(i)])
            E = matmul(RHS, invm) % keysetlen
            D = modMatInv(E, keysetlen)
            print D
            break
    except:
        pass
