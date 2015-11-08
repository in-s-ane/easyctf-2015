fin = open("yuno.jpg")
DATA = fin.read() # Get raw data
fin.close()

counter = 0

print("FOOTER: " + repr(DATA[-2:]))

while counter < len(DATA):
    fout = open("EXTRACTED" + str(counter), 'w')
    fout.write(DATA[counter : len(DATA) - 2])
    fout.close()
    counter += 1

