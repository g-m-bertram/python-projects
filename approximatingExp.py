import math

xValues = [0.001, 0.01, 0.1, 0.99]

for k in xValues:
    x = k

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('x = ' + str(x) + '\n')
    
    eApprox = 0
    exp = math.exp(x)
    eError = exp*0.001
    i = 0
    
    while True:
        eApprox += (x**i) / math.factorial(i)
        i += 1
        if (eApprox >= (exp - eError)) and (eApprox <= (exp + eError)):
            break

    print('Approximation of e^x within 0.1%:\t' + str(eApprox) + ' (' + str(i) + ' terms)')
    print('Actual value of e^x:\t\t\t' + str(exp) + '\n')
    

    lnApprox = 0
    ln = math.log(1+x)
    lnError = ln*0.001
    j = 1

    while True:
        lnApprox += (-1)**(j+1) * (x**j) / j
        j += 1
        if (lnApprox >= (ln - lnError)) and (lnApprox <= (ln + lnError)):
            break

    print('Approximation of ln(1+x) within 0.1%:\t' + str(lnApprox) + ' (' + str(j) + ' terms)')
    print('Actual value of ln(1+x):\t\t' + str(ln))
