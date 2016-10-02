'''import math   #firstly you should import the library

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print x,y



def add_end(L=[]):
    L.append('end')
    return L

a=add_end([1,2,3])
print a
'''

