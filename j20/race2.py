sec,prog,speed=0,0,0
def stay(x):
   global sec, prog, speed
   for i in range(x):
      prog+=speed
      sec+=1 
def increaseSpeed(x):
   global sec, prog, speed
   for i in range(x):
      speed+=1
      stay(1)
def decreaseSpeed(x):
   global sec, prog, speed
   for i in range(x):
      speed-=1
      stay(1) 
def main():
   fin = open ('race.in', 'r')
   fout = open ('race.out', 'w')
   n=fin.readline().strip().split()
   n=[int(i) for i in n]
   x=fin.read().rstrip().split()
   x=[int(i) for i in x]
   print n,x
   for i in range(n[1]):
      sec,prog,speed=0,0,0
      increaseSpeed(x[i])
      sec1,prog1,speed1=sec,prog,speed
      increaseSpeed(1)
      while prog<n[0]:
         if speed+prog>n[0]:
            decreaseSpeed(1)
         stay(1)
         print prog,sec
   fout.close()
if __name__ == '__main__':
    main()  
