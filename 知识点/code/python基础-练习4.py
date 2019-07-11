'''
def text(a,b,*args,**kwargs):
        print(a)
        print(b)
        print(args)
        print(kwargs)
a = (1,2)
b = {"dfd":"dfsd"}
text(1,2,8,9,63,2,*a,**b)
'''
''' 
def getNum(num):
        if num > 1: 
                return num*getNum(num-1)
        else: 
                return num
        
                
a=getNum(4)
print(a)
    
    
''' 
