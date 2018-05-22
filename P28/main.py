def lsort(x):
    x.sort(key = len)
    return x

def lfsort(x):
    list = []
    for i in x:
        if list == []:
            list.append([i])
        else:
            is_added = False
            for j in list:
                if len(j[-1]) == len(i):
                    j.append(i)
                    is_added = True
            if is_added == False:
                list.append([i])
    list.sort(key = len)

    flat = []
    for k in list:
        flat = flat + k
    return(flat)
