fin = open ('backforth.in', 'r')
fout = open ('backforth.out', 'w')
b1=fin.readline().split()
b2=fin.readline().split()
for i in range(len(b1)):
   b1[i]=int(b1[i])
   b2[i]=int(b2[i])
#tue buck, wed buck, thurs buck, all iteration of fri buck
ob1=b1
ob2=b2
milk=1000
bad=0
answers=[]
for i in range(len(b1)):
   b2.append(b1[i])
   milk-=b1[i]
   for j in range(len(b2)):
      b1.append(b2[j])
      milk+=b2[j]
      for k in range(len(b1)):
         b2.append(b1[k])
         milk-=b1[k]
         for l in range(len(b2)):
            milk+=b2[l]
            for m in range(len(answers)):
               if milk==answers[i]:
                  bad=1
            if bad!=1:
               answers.append(milk)
            milk=0
         