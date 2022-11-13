def test():
    print(1)

test()


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
ans = is_prime(17)
print(ans)

