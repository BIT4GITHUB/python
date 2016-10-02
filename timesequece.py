print "Please choose the alogrithme:"
print "0.Exit"
print "1.FIFO"
print "2.SJF"
print "3.LJF"
list=[[0,7],[3,3],[6,9],[9,2]]
a=raw_input("Input:\n")
def FIFO():
    list.sort()
    for k in range(len(list)):
        print "process %d",int(k)
        list[k][0]=int(raw_input("input the come time:"))
        list[k][1]=int(raw_input("input the severce time:"))
    
    T1=list[0][1]+(list[0][1]-list[1][0]+list[1][1])+(list[0][1]+list[1][1]-list[2][0]+list[2][1])+(list[0][1]+list[1][1]+list[2][1]-list[3][0]+list[3][1])
    t1=float(T1)/len(list)
    T2=list[0][1]/list[0][1]+(list[0][1]-list[1][0]+list[1][1])/list[1][1]+(list[0][1]+list[1][1]-list[2][0]+list[2][1])/list[2][1]+(list[0][1]+list[1][1]+list[2][1]-list[3][0]+list[3][1])/list[3][1]
    t2=float(T2)/len(list)
    print "FIFO time:\nMean:%f\nAnother:%f"%(t1,t2)

def SJF():
    list.sort()
    T1=list[0][1]+(list[0][1]-list[1][0]+list[1][1])+(list[0][1]+list[1][1]-list[3][0]+list[3][1])+(list[0][1]+list[1][1]+list[3][1]-list[2][0]+list[2][1])
    t1=float(T1)/len(list)
    T2=list[0][1]/list[0][1]+(list[0][1]-list[1][0]+list[1][1])/list[1][1]+(list[0][1]+list[1][1]-list[3][0]+list[3][1])/list[2][1]+(list[0][1]+list[1][1]+list[3][1]-list[2][0]+list[2][1])/list[3][1]
    t2=float(T2)/len(list)
    print "SJF time:\nMean:%f\nAnother:%f"%(t1,t2)

def LJF():
    list.sort()
    T1=list[0][1]+(list[0][1]-list[1][0]+list[1][1])+(list[0][1]+list[1][1]-list[2][0]+list[2][1])+(list[0][1]+list[1][1]+list[2][1]-list[3][0]+list[3][1])
    t1=float(T1)/len(list)
    T2=list[0][1]/list[0][1]+(list[0][1]-list[1][0]+list[1][1])/list[1][1]+(list[0][1]+list[1][1]-list[2][0]+list[2][1])/list[2][1]+(list[0][1]+list[1][1]+list[2][1]-list[3][0]+list[3][1])/list[3][1]
    t2=float(T2)/len(list)
    print "LJF time:\nMean:%f\nAnother:%f"%(t1,t2)

if int(a)==0:
    print "exit"
elif int(a)==1:
    FIFO()
elif int(a)==2:
    SJF()
else:
    LJF()


        
