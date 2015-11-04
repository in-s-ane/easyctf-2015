message = "hello world"

key = 3

encrypted = ' '.join([str(ord(c)//key) for c in message])
print(encrypted)

f = open("floors.txt", 'r').read().split()

noShift = []
shiftOne = []
shiftTwo = []

for i in f:
    noShift.append(chr(int(i) * key))
    shiftOne.append(chr(int(i) * key + 1))
    shiftTwo.append(chr(int(i) * key + 2))

print ''.join(noShift)
print ''.join(shiftOne)
print ''.join(shiftTwo)
