!#/usr/bin/env python3

import travelmethods as tm
from travelmethods import *

# set constants
R = 6371.0
# assume average P velocity
vp = 11.
# rpd is radians per degree
rpd = math.pi/180.
# kpd is km per degree
kpd = R*rpd
# set earthquake origin time:
Oh=4
Om=49
Os=20

# initialize lists:
distances = []
t0s=[]
# opens the date file ptimescopies, which has the header deleted all but P #and np columns
ptm = open('Ptimescopies.txt','r')
for line in ptm:
 fields = line.split() 
# splits lines into fields and fields into the distances
 distances = distances + [float(fields[4])]
# the 8th column is time
 time = fields[7].split('Z')[0].split('T')[1].split(':')
# subtract origin time to obtain travel time:
 seconds = 3600*(float(time[0])-Oh)+60*(float(time[1])-Om)+float(time[2])-Os

# Measuring along earths surface chord
for d in distances:
   b = d*kpd
# Then convert to distances, d
   t1 = b/vp
   print('%g  %g' % (d,t1))
# calculate theoretical travel times using the chord method for all distances #at which we have observations


#tm.t1(distances)

#plot(distances,t1s,'blue')
#plot(distances,t2s,'red')
#show( )
