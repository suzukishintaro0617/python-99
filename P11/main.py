def encode_modified(x):
    ret_A=[]
    for X in x:
        if(ret_A==[] or ret_A[-1][-1]!=X):
            ret_A=ret_A+[[X]]
        else:
            ret_A[-1].append(X)
        ret_B=[]
        for Y in ret_A:
            if(len(Y)==1):
                ret_B=ret_B+Y
            else:
                ret_B=ret_B+[[len(Y),Y[0]]]
    return ret_B
