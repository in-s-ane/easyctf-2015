f = open("sorting-job.in", "r").read()

_sorted = str(sorted(eval(f))[::-1]).strip("[]").replace(" ", "")

f = open("sorting-job.out", "w").write("%s\n" % _sorted)

# easyctf{sorting_is_as_easy_as_3_2_1!}
