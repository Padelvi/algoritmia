from math import floor

for _ in range(int(input())):
    izq, _, dcha = input().partition("=")

    def separar_terms(s: str,
                      acc_x=(),
                      acc_ind=(),
                      sgn_previo:int=+1,
                      parar_previo=False
    ) -> tuple[tuple,tuple]:
        if parar_previo or not s:
            return acc_x,acc_ind

        pos_seguir = 0
        sgn_posterior = 1
        term = ""
        parar = False

        for i, char in enumerate(s):
            if char in "+-" and term:
                pos_seguir = i+1
                sgn_posterior = 1 if char=="+" else -1
                break
            else:
                term += char
        else:
            parar = True

        # print(term)
        if term[-1] == "x":
            if term == "x":
                acc_x += (sgn_previo,)
            elif term == "-x":
                acc_x += (-sgn_previo,)
            else:
                acc_x += (sgn_previo*int(term[:-1]),)
        else:
            acc_ind += (sgn_previo*int(term),)

        # print(acc_x,acc_ind)
        return separar_terms(s[pos_seguir:],acc_x,acc_ind,sgn_posterior,parar)

    izq_x, izq_ind = map(sum,separar_terms(izq))
    # print(izq_x,izq_ind)
    dcha_x, dcha_ind = map(sum,separar_terms(dcha))
    # print(dcha_x,dcha_ind)

    terms_finales = (izq_x-dcha_x,izq_ind-dcha_ind)

    # print(terms_finales)

    if terms_finales[0] == 0:
        print("IDENTITY" if terms_finales[1] == 0 else "IMPOSSIBLE")
    else:
        print(int(floor(-terms_finales[1]/terms_finales[0])))