def unm(x):
    '''Creates an array of unique elements sorted alphabetically from an array of duplicate elements'''
    return  sorted( set(x) )

def unm2(x):
    '''Creates an array with unique elements from an array with duplicate elements'''
    n = []
    for i in range( len(x) ):
        if x[i] not in x[i+1:] :
            n.append(x[i])
    return n

def uns(x):
    '''Creates a string with unique characters sorted alphabetically from a given string'''
    return  ''.join(  sorted( set(x) )  )

def uns2(x):
    '''Creates a string with unique characters from a given string'''
    s=''
    for i in range( len(x) ):
        if x[i] not in s :
            s += x[i]
    return s

def rmAll(b, x):
    '''Delete all b values from array x'''
    c = True
    while c:
        try:
            x.remove(b)
        except ValueError:
            c = False

def fn(p, m):
    '''All positions of the values of P in the array M. As an array.'''
    z=[]; st=0
    while True:
        try:
            r = m.index(p, st)
            z.append(r)
            st = r+1
        except ValueError:
            return z

def  all_uniq(lst):
    ''' Returns True if all elements are unique '''
    return  len(lst) == len( set(lst) )
