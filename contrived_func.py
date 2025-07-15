import math


def contrived_func(val):
    print(f'====[{val}]====')
    a = val + math.sqrt(abs(val*3)) < 20
    b = val ** 5 % 3 != 0
    c = val * 5 + val / 3 > 200
    d = val ** 2 < 2
    print('conditions:', end=' ')
    print(a, b, c, d)

    path = []
    if a or b:
        path.append('T')
        if (a and b) or (b and c) and d:
            path.append('T')
            pass
        else:
            path.append('F')
            pass
    else:
        path.append('F')
        if (a or b) or (b or c):
            path.append('T')
            pass
        else:
            path.append('F')
            pass
    
    if a and b:
        path.append('T')
        pass
    else:
        path.append('F')
        pass

    print('branches:', end=' ')
    print(" ".join(path))
