import time, datetime

# time module
"""
def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % len(str(prod)))
print('Took %s seconds to calculate.' % (endTime - startTime))
print('Now pausing for 3 seconds.')
time.sleep(3)
print('Done')
"""

# datetime module
print(datetime.datetime.now())
dt = datetime.datetime.now()
print(str(dt.month) + '/' + str(dt.day) + '/' + str(dt.year))
halloween2024 = datetime.datetime(2024, 10, 31, 0, 0, 0)
print('Halloween is ' + str(halloween2024.month) + '/' + str(halloween2024.day))