fin = open ('photo.in', 'r')
fout = open ('photo.out', 'w')
n=int(fin.readline())
a=fin.readline().rstrip().split()
a=[int(i) for i in a] 
print n,a
fout.close()