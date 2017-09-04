### Create "range" number of files with 100 random numbers from 0-1000 scope

import random

for i in range(0, 2):
    f = open("testfile" + str(i) + ".txt", "w")
    for number in range(0, 100):
        f.write(str(random.randrange(1000)))
        f.write("\n")
    f.close()