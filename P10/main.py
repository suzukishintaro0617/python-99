
def encode(elements):
    ret = []
    tmp = [] # working

    for e in elements:
        if not tmp:
            tmp = [e]
        elif tmp and tmp[-1] != e:
            ret.append([len(tmp), tmp[0]])
            tmp = [e]
        else:
            tmp.append(e)

    ret.append([len(tmp), tmp[0]])

    return ret

