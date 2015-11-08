fin = open("yuno.jpg")
DATA = fin.read() # Get raw data
fin.close()

counter = 219

#while counter < 400:
fout = open("EXTRACTED" + str(counter), 'w')
#    fout.write(DATA[counter:len(DATA) - 1])
#    fout.close()
#    counter += 1

