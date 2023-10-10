fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
num=int(fin.readline())
beads=fin.readline().rstrip()
max=0
for j in range(num):
   cur, redbad, bluebad=0,0,0
   i=j
   while (not ((redbad==1 and beads[i]=='r') or (bluebad==1 and beads[i]=='b'))) and cur!=num:
      if beads[i]=='r':
         bluebad=1
      if beads[i]=='b':
         redbad=1
      cur+=1
      i+=1
      if i==num: i=0
   redbad, bluebad=0,0
   i=j-1
   if i==-1: i=num-1
   while (not ((redbad==1 and beads[i]=='r') or (bluebad==1 and beads[i]=='b'))) and cur!=num:
      if beads[i]=='r':
         bluebad=1
      if beads[i]=='b':
         redbad=1
      cur+=1
      i-=1
      if i==-1: i=num-1
   if cur>max: max=cur
fout.write (str(max) + '\n')
fout.close()