import random
import sys
import os
import global_settings as gs
import test1
import test2

# seed = random.randrange(sys.maxsize)
# file = open("seed.txt" , "w")
# file.write(str(seed))

if gs.rerun and os.path.exists("seed.txt"):
    file = open("seed.txt")
    lines = file.read().splitlines()[0]
    seed = int(lines)
    random.seed(seed)
else:
    new_seed = random.randrange(sys.maxsize)
    file = open("seed.txt", "w")
    file.write(str(new_seed))
    random.seed(new_seed)




test1.test1()
test2.test2()


