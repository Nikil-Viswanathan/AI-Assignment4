#TWO + TWO = FOUR

letters = ['T','W','O','F','U','R']
carries = ['c1','c2','c3']

def valid(a):

    #all letters should have different digits
    vals = [a[x] for x in letters if x in a]
    if len(vals) != len(set(vals)):
        return False

    #leading digits can't be 0
    if 'T' in a and a['T'] == 0:
        return False
    if 'F' in a and a['F'] == 0:
        return False


    # O + O
    if all(x in a for x in ['O','R','c1']):
        if (a['O'] + a['O']) % 10 != a['R']:
            return False
        if (a['O'] + a['O']) // 10 != a['c1']:
            return False

    # W + W + c1
    if all(x in a for x in ['W','U','c1','c2']):
        if (a['W']*2 + a['c1']) % 10 != a['U']:
            return False
        if (a['W']*2 + a['c1']) // 10 != a['c2']:
            return False

    # T + T + c2
    if all(x in a for x in ['T','O','c2','c3']):
        if (a['T']*2 + a['c2']) % 10 != a['O']:
            return False
        if (a['T']*2 + a['c2']) // 10 != a['c3']:
            return False

    # last carry becomes F
    if 'c3' in a and 'F' in a:
        if a['c3'] != a['F']:
            return False

    return True



def solve(a, vars):

    if len(a) == len(vars):
        return a

    for v in vars:
        if v not in a:
            curr = v
            break

    if curr in carries:
        domain = [0,1]
    else:
        domain = list(range(10))

    for val in domain:
        a[curr] = val

        if valid(a):
            res = solve(a, vars)
            if res:
                return res

        del a[curr]  

    return None


vars = letters + carries
ans = solve({}, vars)

if ans:
    print("\nSolution:\n")
    for k in sorted(ans):
        print(k, "=", ans[k])

    T,W,O,F,U,R = [ans[x] for x in ['T','W','O','F','U','R']]

    two = 100*T + 10*W + O
    four = 1000*F + 100*O + 10*U + R

    print("\nCheck:")
    print(" ", two)
    print("+", two)
    print("------")
    print(" ", four)

else:
    print("No solution")