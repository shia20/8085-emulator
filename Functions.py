def mov(Rd, Rs):
    Rd = Rs

def mov(a, b, **kwargs):
    c = kwargs.get('c', 10)
    d = kwargs.get('d', 20)
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")