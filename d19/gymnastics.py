fin = open ('gymnastics.in', 'r')
fout = open ('gymnastics.out', 'w')
n=fin.readline().strip().split()
#essay=fin.readline().rstrip().split()
n=[int(i) for i in n]
print n
time=[]
for i in range(n[0]):
   q=fin.readline().strip().split()
   q=[int(k) for k in q]
   time.append(q)
for i in range(n[1]):
   for j in range(1,n[1]):
      if time[0][i]>time[0][j]:
         fBig=True
      else:
         fBig=False
#length=len(essay[0])
#fout.write (essay[0])
#fout.write ('\n'+essay[i])  
fout.close()