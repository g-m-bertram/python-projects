import math

x = 5 # some arbitrary value of x
y = x * math.sin(x**2)
dydx = math.sin(x**2) + 2 * x**2 * math.cos(x**2)
dydxError = dydx * 0.000001 # within 0.0001%

h = 1
while h != 0:
    
    yPrime = ((x+h) * math.sin((x+h)**2) - y) / h

    if math.fabs(yPrime) >= math.fabs(dydx - dydxError) and \
            math.fabs(yPrime) <= math.fabs(dydx + dydxError):
        break

    h *= 0.1


print(
        "Actual value of dy/dx at x:\t" + str(dydx) + "\n" +
        "Computed value of dy/dx at x:\t" + str(yPrime) + "\n" +
        "We are able to get a value within 0.0001% of the actual " +
        "value when\nh = " + str(h)
        )
