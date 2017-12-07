#!/usr/bin/env python
import math
import matplotlib.pyplot as plt
#import travelmethods.py

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
 t0s = t0s + [seconds]

# Measuring along earths surface chord
t1s = []
for d in distances:
   b = d*kpd
# Then convert to distances, d
   
   t1 =  b/vp
   #print(t1s)
   #print('%g  %g' % (d,t1))
   #plt.plot(distances,t1,'blue')
   #plt.scatter(d,t1)
   #plt.show()
   #plt.plot(t0s, distances, 'o', color='black');
   t1s = t1s + [t1]
#print (t1s)

t2s = []
for d in distances:
   th = d*rpd
   hth = 0.5*th
# convert radians k
   a = 2*R*math.sin(hth)
   t2 = a/vp
   #print('%g  %g' % (d,t2s))
   #plt.plot(d,t2s, 'o', color='black')
t2s = t2s + [t2]

pairedlist = zip(t0s,t0s)
res1 = [t0-t1 for t0,t1 in pairedlist]
#print(res1[2])