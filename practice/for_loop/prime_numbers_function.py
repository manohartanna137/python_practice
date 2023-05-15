def prime_numbers(m,n):
    for num in range(m,n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num,end=" ")

prime_numbers(1,10)


