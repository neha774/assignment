a = 10
def f():
 print ('Inside f() : ', a)
def g():
 a = 20
 print ('Inside g() : ',a)
def h():
 global a
 a = 30
 print ('Inside h() : ',a)
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)
"""0utput:-
PS C:\Gobind kumar> python -u "c:\Gobind kumar\2004812\main.py"
global :  10    
Inside f() :  10
global :  10    
Inside g() :  20
global :  10    
Inside h() :  30
global :  30    
PS C:\Gobind kumar> 
"""
