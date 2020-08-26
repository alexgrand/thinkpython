def do_twice(f, val):
    f(val)
    f(val)

def print_spam(vl):
    print(vl)

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

do_twice(print, 'spam')
print('')

do_four(print, 'spam')