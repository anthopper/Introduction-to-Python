#!/usr/bin/env python3

R = 6371.0
vp = 11.0
import math
kpd=R*math.pi/180.
Oh = 4
Om = 49
Os = 20
t0s= []
distances = []
datafile = open('Ptimescopies.txt','r')


dstep = 1.
d = 0.
while d <= 100.:
     k = d*kpd
     t = k/vp
     #print('%g  %g' % (d,t))
     d = d + dstep
     

datafile = open('Ptimescopies.txt','r')
#lines = datafile.readlines()[1:]
for line in datafile:
     fields = line.split()
     distances = distances + [float(fields[4])]
     fields = line.split()
     distances = distances + [float(fields[4])]
     time = fields[7].split('Z')[0].split('T')[1].split(':')
     seconds = 3600*(float(time[0])-Oh) + 60*(float(time[1])-Om) + float(time[2])-Os
     t0s = t0s + [seconds]
     print(line)
     print(seconds)

t1s = []
for d in distances:
     k = d*kpd
     t = k/vp
     t1s = t1s + [t]
#print(distances)
#print(t0s)
#print(t1s)

print(47777777)
for line in datafile:
     a = [distances, t0s, t1s]
     n = len(a)
     for i in range(n):
          print(a[0], a[1], a[2])
#print(distances)
