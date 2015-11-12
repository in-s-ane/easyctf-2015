from string import ascii_uppercase as v, ascii_lowercase as k
import sys

def check_flag(s):
        # Must be 25 chars long
	if len(s) != 25:
		return False
        print "Checkpoint 1"

	s = list(s)
        # Looks something like this: 1141111111101010101131111, where 1 can be replaced with any number
        if int(`[s.pop(r) for r in [20, 17, 15, 13, 11, 2]][::-1]`[2::5]) != 400003:
		return False
        print "Checkpoint 2"

        # 'h' must be at first index:
        # Now looks something like this: 1h41111111101010101131111
	if len(list(set([s.pop(r) for r in map(lambda p: int(p, 2), ["11", "111"])[::-1]]))) != s.index("h"):
		return False
        print "Checkpoint 3"

	y, z = [], []
	# y and z are the last 4 characters of the input
	u = len(list(set([repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]))) - 1 # u = 0
	print y, z
	if len(list(set(y))) != len(list(set(z))):
		return False
        print "Checkpoint 4"

        # Looks something like this:
        # 1h4111111110101010113zdzd
        # where z and d can be characters when xor'd give 30
	if (ord(y[0]) ^ ord(z[0])) ^ 30 != 0:
		return False
        print "Checkpoint 5"

        # v.index("S") = 18
        # 18 ^ 12 ^ 30 == 0
        # Now looks something like this: 1h41111111101010101S3zdzd
	if v.index(s.pop()) ^ 12 ^ 30 != 0:
		return False
        print "Checkpoint 6"

        # See's whrthoooo....
        # What are those?!?! please tell me thats not the flag...
	a, i = filter(lambda c: c in v, s), filter(lambda c: c in k, s)
	# a is uppercase, i is lowercase
	# Make sure that these characters are within our input
	if [87, 82, 84, 72, 79, 79, 79, 79] != map(ord, a):
		return False
        print "Checkpoint 7"

	i[1:3] = i[2:0:-1]
	if i != list("hate"):
		return False
	return "Got the flag!"

print check_flag(sys.argv[1])

# Note: The grader seems to run the check_flag function on your input, so as long as it passes then it is a valid flag.

# After getting past checkpoint 6, it was clear what the flag probably was.
# Playing around with the values, I was able to guess a valid flag (which was also probably the intended one)
# Wh4t_aRe_TH0O0O0O0OS3?!?!
