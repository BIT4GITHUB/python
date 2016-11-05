'''
    *Date:16-10-28
    *Name:时间调度算法.py
'''
#--coding:utf-8--
print "0.Exit"
print "1.FIFO"
print "2.SJF"
print "3.LJF"
list1=[[0,0],[0,0],[0,0],[0,0]]
list=[[0,0],[0,0],[0,0],[0,0]]
a=raw_input("Please choose the Algorithm:")
ft=[0,0,0,0]    #完成时间
tp=[0,0,0,0]    #周转时间
qtt=[0,0,0,0]   #带权周转时间


def FIFO():
    print "==========FIFO Algorithm=============="
    ft=[0,0,0,0];tp=[0,0,0,0];qtt=[0,0,0,0]
    for k in range(4):
        print "process %d"%int(k+1)
        list[k][0]=float(raw_input("input the come time:"))
        list[k][1]=float(raw_input("input the severce time:"))
    list.sort()
    ft[0]=list[0][0]+list[0][1]
    tp[0]=ft[0]-list[0][0]
    qtt[0]=1
    for k in range(1,4):
        if(list[k][0]<ft[k-1]):
            ft[k]=ft[k-1]+list[k][1]
            tp[k]=ft[k]-list[k][0]
            qtt[k]=tp[k]/list[k][1]
        else:
            ft[k]=list[k][0]+list[k][1]
            tp[k]=ft[k]-list[k][0]
            qtt[k]=tp[k]/list[k][1]
    print "周转时间："
    print tp
    print "完成时间："
    print ft
    print "带权周转时间："
    print qtt
    ATP=sum(tp)/4.0;AQTT=sum(qtt)/4.0
    print "the ATP is:%f\nthe AQTT is:%f\n"%(ATP,AQTT)


def SJF():
    print "==========SJF Algorithm=============="
    ft=[0,0,0,0];tp=[0,0,0,0];qtt=[0,0,0,0]
    for k in range(4):
        print "process %d"%int(k+1)
        list[k][1]=float(raw_input("input the come time:"))
        list1[k][0]=list[k][1]
        list[k][0]=float(raw_input("input the severce time:"))
        list1[k][1]=list[k][0]
    list1.sort()
    list.sort()
    print list
    print list1
    ft[0]=list1[0][1]+list1[0][0]
    tp[0]=ft[0]-list1[0][0]
    qtt[0]=ft[0]/list1[0][1]
    del list[list.index([list1[0][1],list1[0][0]])]
    del list1[0]
    print list
    print list1
    for t in range(3):
        if(ft[t]>=list[0][1]):
            ft[t+1]=ft[t]+list[0][0]
            tp[t+1]=ft[t+1]-list[0][1]
            qtt[t+1]=tp[t+1]/list[0][0]
            del list1[list1.index([list[0][1],list[0][0]])]
            del list[0]
        elif(list[0][0]<ft[t]):
            ft[t+1]=ft[t]+list1[0][1]
            tp[t+1]=ft[t+1]-list1[0][0]
            qtt[t+1]=tp[t+1]/list1[0][1]
            del list[list.index([list1[0][1],list1[0][0]])]
            del list1[0]
        else:
            ft[t+1]=list1[0][0]+list1[0][1]
            tp[t+1]=ft[t+1]-list1[0][0]
            qtt[t+1]=tp[t+1]/list1[0][1]
            del list[list.index([list1[0][1],list1[0][0]])]
            del list[0]
        print list
        print list1
    print "周转时间："
    print tp
    print "完成时间："
    print ft
    print "带权周转时间："
    print qtt
    ATP=sum(tp)/4.0;AQTT=sum(qtt)/4.0
    print "the ATP is:%f\nthe AQTT is:%f\n"%(ATP,AQTT)


def LJF():
    print "==========LJF Algorithm=============="
    ft=[0,0,0,0];tp=[0,0,0,0];qtt=[0,0,0,0]
    for k in range(4):
        print "process %d"%int(k+1)
        list[k][1]=float(raw_input("input the come time:"))
        list1[k][0]=list[k][1]
        list[k][0]=float(raw_input("input the severce time:"))
        list1[k][1]=list[k][0]
    list1.sort()
    list.sort(reverse=True)
    ft[0]=list1[0][1]+list1[0][0]
    tp[0]=ft[0]-list1[0][0]
    qtt[0]=ft[0]/list1[0][1]
    del list[list.index([list1[0][1],list1[0][0]])]
    del list1[0]
    for t in range(3):
        if(ft[t]>=list[0][1]):
            ft[t+1]=ft[t]+list[0][0]
            tp[t+1]=ft[t+1]-list[0][1]
            qtt[t+1]=tp[t+1]/list[0][0]
            del list1[list1.index([list[0][1],list[0][0]])]
            del list[0]
        elif(list[0][0]<ft[t]):
            ft[t+1]=ft[t]+list1[0][1]
            tp[t+1]=ft[t+1]-list1[0][0]
            qtt[t+1]=tp[t+1]/list1[0][1]
            del list[list.index([list1[0][1],list1[0][0]])]
            del list1[0]
        else:
            ft[t+1]=list1[0][0]+list1[0][1]
            tp[t+1]=ft[t+1]-list1[0][0]
            qtt[t+1]=tp[t+1]/list1[0][1]
            del list[list.index([list1[0][1],list1[0][0]])]
            del list[0]
    print "周转时间："
    print tp
    print "完成时间："
    print ft
    print "带权周转时间："
    print qtt
    ATP=sum(tp)/4.0;AQTT=sum(qtt)/4.0
    print "the ATP is:%f\nthe AQTT is:%f\n"%(ATP,AQTT)


if int(a)==0:
    print "exit"
elif int(a)==1:
    FIFO()
elif int(a)==2:
    SJF()
elif int(a)==3:
    LJF()
else:
    print "error"


        
