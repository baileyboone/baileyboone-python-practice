if __name__ == "__main__":
    ### declaring
    x = 6
    y = "Bailey"
    ### printing
    print(x)
    print(y)
    ### changing variable data and type
    x = "Boone"
    print("{} {}".format(y, x))
    ### casting
    a = str(3)
    b = int(3)
    c = float(3)
    print("{} {} {}".format(a,b,c))
    ### type()
    for variable in [x, y, a, b, c]:
        print("{} is a {}".format(variable, type(variable)))
    ### case sensitivity
    X = "Not Boone"
    print("{} {}".format(x, X))
    ### naming conventions
    valid = "valid"
    _also = "valid"
    # 1not = "invalid due to leading numeral"
    # alpha_numerical_and_underscore_only? = "invalid due to ? character"
    # and = "invalid due to keyword usage"
    # assert = "invalid due to same"
    # def = "invalid due to same"
    camelCase = "valid"
    PascalCase = "valid"
    snake_case = "valid"
    ### many values to multiple variables
    m, n, o = "em", "en", "oh"
    print("{} {} {}".format(m,n,o))
    ### one value to multiple variables
    p = q = r = "samesies"
    print("{} {} {}".format(p,q,r))
    ### unpacking
    roles = ["Alice", "Bob", "Carol"]
    al, bo, ca = roles
    print("{} {} {}".format(al,bo,ca))
    ### output variables
    i = "I"
    d = "didn't"
    k = "know"
    print(i,d,k)
    print("I could've been doing this the whole time")
    print(k+i+d)
    g = 8
    t = 4
    print(g+t)
    print(t,i,g)
    ### globals
    u = "global"

    def myfunc():
        print("This u is a", u)
    
    myfunc()

    def anotherfunc():
        u = "local"
        print("This u is a", u)
    
    anotherfunc()
    print("And u is still", u)

    def makeglobal(ambition):
        global globe
        globe = ambition
    
    makeglobal("Earth")
    print(globe, "is now global")

    def updateglobe(planet):
        global u
        u = planet
    
    updateglobe("Jupiter")
    print("u is now", u)
