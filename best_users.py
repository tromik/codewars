def id_best_users(*args):
    # your code here
    import pdb; pdb.set_trace()
    return locals()
    for a in args:
        print a



a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a4 = ['A042', 'A025', 'B004']

print id_best_users(a1, a2, a3, a4)
