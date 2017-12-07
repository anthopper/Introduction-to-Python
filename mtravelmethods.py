!#/usr/bin/env python3

from math import radians, sin
def t1(d,R,vp):
   return R*radians(d)/vp
def t2(d,R,vp):
   return 2.*R*sin(radians(0.5*d))/vp

def ht2(ds,R,vp):
    f = 2*R/vp
    return f*np.sin(np.radians(0.5*ds)) 

timecode = "t=ht2(ds,R,vp)"
 scode = "import numpy as np; R=6000; vp=10."
 slist = "dl = [0.0001*i for i in range(1000000)]; ds = np.array(dl)"
 sfunc = "from __main__ import ht2"
 setupall = scode + ";" + slist + ";" + sfunc
 n = 10
 timeit.timeit(timecode,setupall,number=n)

