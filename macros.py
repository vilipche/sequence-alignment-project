def c_sub(x,y):
    if(x==y):
        return 0
    elif((x=="A" and y=="T") or (y=="A" and x=="T") or (x=="G" and y=="C") or (y=="G" and x=="C")):
        return 3
    else:
        return 4

c_del = 2
c_ins = 2

