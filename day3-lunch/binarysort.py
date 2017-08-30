#!/usr/bin/env python

import random
r = random.randint(1,100)

nums = range(0, 100, 10)

print nums
##what we are looking for
key = 17

low = 0
hi = len(nums)


#for i in xrange(len(nums)):
while low < hi:
    mididx = (low + hi) / 2    
    mid = nums[mididx]
    print "checking in the range [%d, %d] mididx[%d]=%d" % (low, hi, mididx, mid)
    
    if (mid == key):
        print "hooray! found it at %d==%d at %d" % (key, mid, mididx) 
        break

    elif (key > mid):
        low = mididx + 1
    else:
        hi = mididx