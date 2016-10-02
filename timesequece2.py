list=[[0,7],[3,3],[6,9],[9,2]]
list.sort()
print list
t=0
for k in range(len(list)):
    t=list[k][1]
    list[k][1]=list[k][0]
    list[k][0]=t
print list
for k in range(len(list)):
    print "process:",int(k+1)
    list[k][0]=int(raw_input("input the come time:"))
    list[k][1]=int(raw_input("input the severce time:"))                 
print list
