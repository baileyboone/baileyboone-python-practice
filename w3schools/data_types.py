if __name__ == "__main__":
    ### text types
    string = "theory"
    print(string)
    cast_string = str("string")
    print(cast_string)

    print()
    ### numeric types
    integer_num = 6
    print(integer_num)
    cast_int = int(12)
    print(cast_int)

    print()
    float_num = 3.14
    print(float_num)
    cast_float = float(804.2)
    print(cast_float)

    print()
    complex_num = 1+2j
    print(complex_num)
    real_part = 1
    imaginary_part = 2
    cast_complex = complex(real_part, imaginary_part)
    print(cast_complex)
    print(cast_complex.real, cast_complex.imag)

    print()
    ### sequence types
    list_seq = ["first", "second", "third", "first"]
    print(list_seq)
    for entry in list_seq:
        print(entry)
    cast_list = list(("third", "second", "first", "third"))
    print(cast_list)
    for entry in cast_list:
        print(entry)

    print()
    tuple_seq = ("first", "second")
    print(tuple_seq)
    for entry in tuple_seq:
        print(entry)
    cast_tuple = tuple(("first", "second"))
    print(cast_tuple)
    for entry in cast_tuple:
        print(entry)

    print()
    range_seq = range(8)
    print(range_seq)
    for entry in range_seq:
        print(entry)
    
    print()
    ### mapping type
    dictionary = {"key": "value", "lock": "key"}
    print(dictionary)
    for entry in dictionary:
        print("curr's key: {}, curr's value: {}".format(entry, dictionary[entry]))
    cast_dict = dict(key="value", lock="key")
    print(cast_dict)
    for entry in cast_dict:
        print("curr's key: {}, curr's value: {}".format(entry, cast_dict[entry]))
    
    print()
    ### set types
    set_type = {"first", "second", "third", "second"}
    print(set_type)
    for member in set_type:
        print(member)
    cast_set = set(("third", "second", "first", "third"))
    print(cast_set)
    for member in cast_set:
        print(member)
    
    print()
    frozen_set = frozenset({"first", "second", "third", "second"})
    print(frozen_set)
    for member in frozen_set:
        print(member)
    cast_frozen = frozenset(("third", "second", "first", "second"))
    print(cast_frozen)
    for member in cast_frozen:
        print(member)
    
    print()
    ### boolean type
    boolean = True
    if boolean:
        print(boolean, "True")
    else:
        print(boolean, "False")
    cast_boolean = bool(-5)
    if cast_boolean:
        print(cast_boolean, "True")
    else:
        print(cast_boolean, "False")
    
    print()
    ### binary types
    portion = b"Hello"
    print(portion)
    meal = bytearray(8)
    print(meal)
    memory = memoryview(bytes(8))
    print(memory)

    print()
    ### None type
    nothing = None
    print(nothing)
    