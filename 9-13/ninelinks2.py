# 九连环拆解，递归算法



def down(n):
    if n>2:
        down(n-2)
        print('卸下',n,'环')
        up(n-2)
        down(n-1)
    if n==2:
        print('卸下 {},{} 环'.format(n,n-1))    
    if n<2:
        print('卸下',n,'环') 
        
def up(n):
    if n>2:
        up(n-1)
        down(n-2)
        print("装上",n,"环")
        up(n-2)
    if n==2:
        print("装上 %d,%d 环" % (n,n-1))
        
    if n<2:
        print("装上",n,"环")
print("拆解")
down(2)
print('---------------------------------\n','装上')
up(3)
print("结束")
