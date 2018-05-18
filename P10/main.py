def encode(x):
    ret_a=[]
    for X in x:
        if(ret_a==[] or ret_a[-1][-1]!=X):
            ret_a=ret_a+[[X]]
        else:
            ret_a[-1].append(X)
        ret_b=[]
        for Y in ret_a:
            ret_b=ret_b+[len(Y),Y[0]]
    return ret_b
