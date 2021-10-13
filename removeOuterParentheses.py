def removeOuterParentheses(s: str) -> str:
    primitives = primitiveDecomposition(s)
    result = removingOuterParentheses(primitives)
    return ''.join(result)

def primitiveDecomposition(s):
    s_com = []
    s_int = 0
    i = -1
    divider = []
    i_prev = 0
    s_out = []
    for l in s:
        i+=1
        if l == '(':
            s_com.append(s_int + 1)
        else:
            s_com.append(s_int - 1)
        s_int = s_com[-1]

        if(s_int == 0):
            divider.append((i_prev, i))
            i_prev = i + 1

    for i, j in divider:
        s_out.append(s[i:j+1])
    return s_out

def removingOuterParentheses(primitives):
    result = []
    for primitiv in primitives:
        if primitiv == '()':
            result.append('')
        elif primitiv[0:2] == '((':
            result.append(primitiv[1:len(primitiv)-1])
        else:
            result.append(primitiv)
    return result

removeOuterParentheses('(()())(())')