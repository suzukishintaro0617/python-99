def drop(x,y):
    ret=[]
    for X in range(len(x)):
        if((X+1) % y != 0):
            ret=ret+[x[X]]
    return ret
