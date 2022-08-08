eid, ename, esal = 1, 'aaa', 10000.56


def emp(eid, ename, esal):
    globals()['eid'] = eid
    globals()['ename'] = ename
    globals()['esal'] = esal


print(eid, ename, esal)


def disp():
    print(eid, ename, esal)


emp(111, 'ratan', 10000.45)
disp()
print(eid, ename, esal)
"""
output:-
PS C:\Users\Dell\Documents\assignment-3> python -u "c:\Users\Dell\Documents\assignment-3\q7.py"
1 aaa 10000.56    
111 ratan 10000.45
111 ratan 10000.45
PS C:\Users\Dell\Documents\assignment-3> 
"""