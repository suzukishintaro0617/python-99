def decode(x):
    ret=[]
    for A in x:
        if(isinstance(A,list)):
            ret=ret+[A[-1]]*A[0]
        else:
            ret.append(A)
    return ret
