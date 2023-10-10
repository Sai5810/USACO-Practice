fin = open ('race.in', 'r')
f = open ('race.out', 'w')
n=fin.readline().strip().split()
n=[int(i) for i in n]
x=fin.read().rstrip().split()
x=[int(i) for i in x]
sec,prog,speed=0,0,0
for i in range(x[0]):
   speed+=1
   sec+=1
   prog+=speed
sec1,prog1,speed1=sec,prog,speed
speed1+=1
sec1+=1
prog1+=speed1
while prog1<n[0]:
   if speed1+prog1>n[0]:
      speed1-=1
      sec1+=1
      prog1+=speed1
   else:
      sec1+=1
      prog1+=speed1
f.write(str(sec)+'\n')
f.close()