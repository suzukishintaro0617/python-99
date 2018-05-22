def lsort(x):
    x.sort(key=len)
    return x

def lfsort(x):
    ret=[]
    for i in x:
        if(ret==[]):
            ret.append([i])
            print(ret)
        else:
            is_added = False
            for j in ret:
                if len(j[-1])==len(i):
                    j.append(i)
                    print(ret)
                    is_added = True
            if is_added == False:
                ret.append([i])
                print(ret)
    ret.sort(key=len)

    retA=[]
    for k in ret:
        retA = retA + k
    return(retA)
