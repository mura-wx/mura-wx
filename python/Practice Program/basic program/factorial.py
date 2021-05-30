def factorial(n):
    if n < 0 :
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact*=n
            n -=1 # ini maksdunya pertama 1 * 5 * 4 * 3 * 2
            print (fact)
        return fact

num = 5
print('factorial of ', num, "is", factorial(num))