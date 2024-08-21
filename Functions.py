def MOV(Rd, Rs):
    Rd = Rs

def MOV(a, b, **kwargs):
    c = kwargs.get('c', 10)
    d = kwargs.get('d', 20)
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")