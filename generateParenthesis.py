# # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from random import choice

def generateParenthesis(n: int):
    output = []
    L = 0
    L_max = pow(2, n*2)
    outputValidated = []
    while L < L_max:
        s = ''.join(choice('()') for i in range(n*2))
        if s not in output:
            output.append(s)
            L=L+1
    for i in range(len(output)):
        # output[i] = '(' + output[i] + ')'    
        validateResult = validateParenthesis(output[i])
        if validateResult == 1:
            outputValidated.append(output[i])
    print(outputValidated)

def validateParenthesis(s):
    result = 1
    sum_com = 0
    if s.count('(') != s.count(')'):
        result = 0
    for i in range(len(s)):
        if s[i] == '(':
            sum_com = sum_com + 1
        elif s[i] == ')':
            sum_com = sum_com - 1
        if sum_com < 0:
            result = 0

    return result

generateParenthesis(3)
