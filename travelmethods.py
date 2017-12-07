from math import radians, sin
def t1(d,R,vp):
   return R*radians(d)/vp

def t2(d,R,vp):
   return 2.*R*sin(radians(0.5*d))/vp


def at2(ds,R,vp):
   f=2.*R/vp
   return [f*sin(radians(0.5*x)) for x in ds]