# returns Collatz sequence of a given integer
# will always reach 1 eventually

def collatz(number):
    if (number == 1):
        print(number)
        return 1;
    if number % 2 == 0:
        print(number // 2)
        number = number // 2
    else:
        print(3 * number + 1)
        number = 3 * number + 1
    return collatz(number)
    
print('enter an integer: ')
num = int(input())
while collatz(num) != 1:
    print(collatz(num))