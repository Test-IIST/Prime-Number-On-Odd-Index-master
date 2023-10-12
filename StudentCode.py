#you can set testIO as parameter if user input takes place or anything else dependin on assignment 
#always output through testIO.print() and sure to return testIO 

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def runner(testIO,n):
    ## Enter Student code in this block
    arr=n
    max_prime = float('-inf')
    max_prime_index = -1

    for i in range(1, len(arr), 2):
        if is_prime(arr[i]) and arr[i] > max_prime:
            max_prime = arr[i]
            max_prime_index = i
    testIO.print(max_prime_index)
    ##
    return testIO
