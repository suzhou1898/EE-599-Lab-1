import random
import sys
file=open("input_code2.txt","r+")
i=0
a=[]
for line in file:
   a.insert(i,int(line))
   i=i+1
file.close
random.seed(a[0])
t=[]
for j in range (a[1]):
   t.insert(j,random.randint(a[2],a[3]))
t=list(set(t))
t.sort()
e=len(t)
f=e/5
g=e%5
file=open("output_code2.txt","w+")
file.write("counter integers\n")
for j in range (f):
   file.write("%d: %d,%d,%d,%d,%d\n" % (j*5+1,t[j*5],t[j*5+1],t[j*5+2],t[j*5+3],t[j*5+4]))
if g!=0:
   file.write("%d: " % (f*5+1))
   for j in range (g):
      if j<g-1:
         file.write("%d," % t[f*5+j])
      else: 
         file.write("%d\n" % t[5*f+j])
file.close
