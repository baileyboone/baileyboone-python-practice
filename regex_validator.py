tests_len = int(input())
for i in range(tests_len):
    regex = input()
    valid = True
    escape = False
    repeat = False
    brackets = False
    parans = 0
    braces = False
    brace_contents = "1234567890,"
    prev = None
    length = len(regex)
    for i in range(length):
        if escape:
            escape = False
            prev = regex[i]
            continue
        ex = regex[i]
        if ex == '\\':
            if i+1 == length:
                valid = False
                break
            else:
                escape = True
        else:
            if braces:
                if ex == '}':
                    if (regex[i-2] == '{' or regex[i-2] == ',') and prev == ',':
                        valid = False
                        break
                    else:
                        braces = False
                elif ex not in brace_contents:
                    valid = False
                    break
            elif ex == '{':
                braces = True
            elif ex in ['?', '*', '+']:
                if repeat:
                    # print("double repeat")
                    valid = False
                    break
                else:
                    if prev is None:
                        # print("can't repeat at start of regex")
                        valid = False
                        break
                    else:
                        repeat = True
            else:
                repeat = False
                if ex == '^':
                    if prev: # prev = None means beginning of regex, which is valid for ^
                        if prev != '[':
                            valid = False
                            break
                elif ex == '$':
                    if i+1 != length:
                        valid = False
                        break
                elif ex == '[':
                    brackets += 1
                elif ex == ']':
                    if brackets == 0:
                        print("can't place ] before [")
                        valid = False
                        break
                    else:
                        brackets -= 1
                elif ex == '(':
                    parans += 1
                elif ex == ')':
                    if parans == 0:
                        print("can't place ) before (")
                        valid = False
                        break
                    else:
                        parans -= 1
        prev = ex
    if brackets != 0 or parans != 0:
        print("invalid # of brackets[{}] or parantheses({})".format(brackets, parans))
        valid = False
    print(valid)