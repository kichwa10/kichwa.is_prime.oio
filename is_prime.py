def is_prime(n):

    if n >= 2:
        for x in range (2, n):
            if not (n % x):
                return False
        return True
    else:
        return False
    
    print(is_prime(9))
