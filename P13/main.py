def encode_direct(x):
    ret=[]
    for i in x:
        if(ret==[]):
            ret=ret+[i]
        else:
            if(isinstance(ret[-1],list)):
                if(i==ret[-1][-1]):
                    ret[-1][0]=ret[-1][0]+1
                else:
                    ret.append(i)
            else:
                if(i==ret[-1]):
                    ret[-1]=[2,i]
                else:
                    ret.append(i)
    return ret
