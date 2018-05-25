def encode(x):
    list_a=[]
    for i in x:
        if ( list_a == [] or list_a[-1][-1] != i ):
            list_a = list_a + [[i]]
        else:
            list_a[-1].append(i)

        list_b = []
        for j in list_a:
            list_b = list_b + [[len(j),j[0]]]

    return list_b
