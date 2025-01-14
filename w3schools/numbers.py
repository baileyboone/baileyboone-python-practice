import random

def print_all(args):
    for thing in args:
        print(thing)
        print(type(thing))
    print()

def ints():
    x = 1
    y = 3215798067819320
    z = -312567898094378957621878906874563567687798452345
    all = [x,y,z]
    print_all(all)

def floats():
    x = 1.0
    y = 1.1111111110
    z = -13578.47847476
    a = 65e2
    b = 228E9
    c = -1.24521112e197
    all = [x,y,z,a,b,c]
    print_all(all)

def complexes():
    x = 2+1j
    y = 0-5j
    y2 = -5j
    y3 = complex(0, 8)
    z = -47+0j
    z2 = complex(-47,0)
    all = [x,y,y2,y3,z,z2]
    print_all(all)

def converts():
    x = 1
    y = 3.14

    a = float(x)
    b = int(y)
    c = complex(x)
    d = complex(y)
    all = [x,y,a,b,c,d]
    print("DISCLAIMER:")
    print("Complex numbers cannot be cast into another number type.")
    print_all(all)


def randoms():
    # random has been imported at top of file
    print("Random number:", random.randrange(1, 100))

if __name__ == "__main__":
    ints()
    floats()
    complexes()
    converts()
    randoms()