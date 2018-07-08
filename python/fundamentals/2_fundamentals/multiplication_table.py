i = 1
print "-" * 60
while i < 13:
    n = 1
    while n <= 12:
        print "%4d" % (i * n),
        n += 1
    print ""
    i += 1
print "-" * 60