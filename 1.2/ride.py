fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
ufo=fin.readline()
group=fin.readline()
ufosum, groupsum=1,1
for i in range(len(ufo)):
   ufosum*=ord(ufo[i])-64
for i in range(len(group)):
   groupsum*=ord(group[i])-64
if groupsum%47==ufosum%47:
   fout.write ("GO" + '\n')
else:
   fout.write ("STAY" + '\n')
fout.close()