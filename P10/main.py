def encode(x):
    ret_a=[]
    for i in x:
        if ( ret_a == [] or ret_a[-1][-1] != i ):
            ret_a = ret_a + [[i]]
        else:
            ret_a[-1].append(i)

        ret_b = []
        for j in ret_a:
            ret_b = ret_b + [[len(j),j[0]]]

    return ret_b
