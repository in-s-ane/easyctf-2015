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
		raise ArithmeticError('modular inverse does not exist');
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

def to_row_major(A):    # takes in a column majored array and row majors it
    row_major = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        row_major.append(row)
    return row_major

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

oldcolumn = [0] * blocksize

for i in range(0, len(plaintext), blocksize):
    column = [0] * blocksize
    for j in range(0, blocksize):
        column[j] = oldcolumn[j]^plaintext[i + j]
    oldcolumn = column
    pmatrix.append(column)

cmatrix = []

for i in range(0, len(ciphertext), blocksize):
    column = []
    for j in range(i, i + blocksize):
        column.append(ciphertext[j])
    cmatrix.append(column)

RHS = []
doublecheckC = to_row_major(cmatrix)
pcheck = to_row_major(pmatrix)

a = open("output2", 'rb').read()
flagenc = []
for i in a:
    flagenc.append(ord(i))

fmatrix = []

for i in range(0, len(flagenc), blocksize):
    column = []
    for j in range(i, i + blocksize):
        column.append(flagenc[j])
    fmatrix.append(column)

fmatrix = to_row_major(fmatrix)



#print pmatrix
for subset in combinations(pmatrix, 16):
    RHS = []
    try:
        subset2 = to_row_major(subset)
        invm = modMatInv(subset2, keysetlen)
        if invm[0][0] == int(invm[0][0]):
            for i in subset:
                RHS.append(cmatrix[pmatrix.index(i)])
            RHS = to_row_major(RHS)
            E = matmul(invm, RHS) % keysetlen
            checkC = matmul(E, pcheck) % keysetlen
            D = modMatInv(E, keysetlen)
            final = matmul(D,fmatrix) % keysetlen
            final = to_row_major(final)
            flag = ""
            for i in final:
                for j in i:
                    flag += chr(int(j))

            print flag
    except ArithmeticError:
        pass
