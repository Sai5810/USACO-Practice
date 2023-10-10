fin = open ('word.in', 'r')
fout = open ('word.out', 'w')
n=fin.readline().strip().split()
essay=fin.readline().rstrip().split()
n=[int(i) for i in n] 
length=len(essay[0])
fout.write (essay[0])
print n, essay
for i in range(1,n[0]):
   if length+len(essay[i])<=n[1]:
      fout.write (' '+essay[i])
      length+=len(essay[i])
   else:
      length=len(essay[i])
      fout.write ('\n'+essay[i])  
fout.close()