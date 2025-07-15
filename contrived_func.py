import math


def contrived_func(val):
    a = val + math.sqrt(abs(val*3)) < 20
    b = val ** 5 % 3 != 0
    c = val * 5 + val / 3 > 200
    d = val ** 2 < 2

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
    
    branch_filter = ""
    # conditions_filter = ""
    
    branch_str = " ".join(path)
    conditions_str = " ".join(['T' if var else 'F' for var in [a, b, c, d]])
    # print('----------')
    # print(branch_filter)
    # print(branch_str)
    # print(conditions_str)
    if branch_filter in branch_str:
        print(f'====[{val}]====')
        print(f'branch: {branch_str}')  
        print(f'conditions: {conditions_str}')
