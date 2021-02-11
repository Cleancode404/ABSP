def collatz_sequence(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n //2
        else:
            n = 3*n + 1
            
    else:
        print(n)
        return n 


print(collatz_sequence(3))