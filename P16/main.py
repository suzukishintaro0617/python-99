def drop(x,y):
    ret=[]
    for X in x:
        if(X % y != 0):
            ret=ret+[X]
    return ret
