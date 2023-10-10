fin = open ('race.in', 'r')
n=fin.readline().strip().split()
n=[int(i) for i in n]
for i in range(n[1]):
   minspeed=fin.readline().rstrip()
   minspeed=int(minspeed)
   lhs,rhs,timeused,curr=0,0,0,1
   while True:
      lhs+=curr
      timeused+=1
      if lhs+rhs>=n[0]:
         print timeused
         break
      if curr>=minspeed:
         rhs+=curr
         timeused+=1
         if lhs+rhs>=n[0]:
            print timeused
            break
      curr+=1
   
   
   
   
   
