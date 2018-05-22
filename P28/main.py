def lsort(x):
    x.sort(key = len)
    return x

def lfsort(x):
    ret = []
    for i in x:
        if ret == []:
            ret.append([i])
        else:
            is_added = False
            for j in ret:
                if len(j[-1]) == len(i):
                    j.append(i)
                    is_added = True
            if is_added == False:
                ret.append([i])
    ret.sort(key = len)

    flat = []
    for k in ret:
        flat = flat + k
    return(flat)
