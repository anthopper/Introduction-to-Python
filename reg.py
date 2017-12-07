#!/usr/bin/env python3
import re
fname = 'Ptimes.txt'
lines = open(fname,'r').readlines()


#ptrn = '\s[psPS][CIJKPSa-fimnpsz0-9]*\s'
#ptrn = '[A-Z][A-Z]?\s[A-Z][A-Z][A-Z]*\s[A-Z][A-Z][ZNE12]'
ptrn = '\d+-\d+-\d+T\d+:\d+:\d+.\d+Z'
for line in lines:
   finds = re.finditer(ptrn,line)
   #for f in finds:
      #print(f.group(),f.start())

ms = re.match(ptrn,line) 
print(ms)

fname = 'Ptimes.txt'
fnewa = 'Ptimes.csv'
cold = '\t'
cnew = ','
open(fnewa,'w').write(open(fname,'r').read().replace(cold,cnew))



