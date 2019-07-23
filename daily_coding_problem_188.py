'''
What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?
'''

# This function will print out the number '3' 3 times

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(x):
            print(x)
        flist.append(print_i(i))

    return flist

functions = make_functions()
for f in functions:
    f
# or we can do it this way:

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(x):
            print(x)
        flist.append((print_i, i))

    return flist

functions = make_functions()
for f, arg in functions:
    f(arg)
#
