import random
import sys
import test1
import test2

seed = random.randrange(sys.maxsize)
parent_gen = random.Random(seed)
print("This is the seed" , parent_gen)

test1.test1()
test2.test2()


