def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# print(f1(1,2))
# print(f1(1,2,3))
# print(f1(1,2,3,4,5))
# print(f1(1,2,3,4,5,6,x=1))
print(f2(1,2,3,d=4,x=5,y=4))
args =(1,2,3,4,5)
kw={'x':2,'y':6}
print(f1(*args,**kw))

