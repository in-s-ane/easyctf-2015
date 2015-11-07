fin = open("yuno.jpg")
DATA = fin.read() # Get raw data
fin.close()

fout = open("EXTRACTED", 'w')
fout.write(DATA[219:])
fout.close()

