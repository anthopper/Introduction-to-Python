#!/usr/bin/env python3

R = 6371.0
vp = 11.
AngularDistance = 65
import math
kpd = R*math.pi/180.
print (kpd)

dstep = 1
d = 0.
while d <= 100.:
     print (d)
     d = d + dstep