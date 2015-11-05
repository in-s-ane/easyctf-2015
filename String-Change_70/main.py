fin = open("string-change.in")
fout = open("string-change.out", 'w')

data = fin.read().split("\n")
array = data[0].split(",")

fin.close()

inced = []

for item in array:
    n = int(item)
    counter = n
    while counter < len(data[1]):
        if counter not in inced:
            data[1] = data[1][0:counter] + chr(ord(data[1][counter]) + 1) + data[1][counter + 1:]
        inced.append(counter)
        counter += n

data[1] = data[1].replace("{","a").replace("[","A")

fout.write(data[1] + "\n")
fout.close()

